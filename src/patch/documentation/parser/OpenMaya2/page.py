import logging
import uuid
import bs4

from .. import cached_request, interface

logger = logging.getLogger(__name__)

RANDOM_UUID = str(uuid.uuid4())


def get_memitems(soup: bs4.BeautifulSoup, header_text: str):
    # find the header
    header = soup.find('h2', class_='groupheader', string=header_text)
    if not isinstance(header, bs4.element.Tag):
        return []

    # Go through each next sibling
    current = header.next_sibling
    while current:
        # Check if we've reached another h2 (next section)
        if isinstance(current, bs4.element.Tag) and current.name == 'h2':
            break

        # If it's a div with class "memitem", add it to our list
        if isinstance(current, bs4.element.Tag) and current.name == 'div':
            current_classes = current.get('class')
            if current_classes:
                # Handle both string and list formats for class attribute
                if isinstance(current_classes, str):
                    class_list = [current_classes]
                else:
                    class_list = current_classes

                if 'memitem' in class_list:
                    yield current

        current = current.next_sibling


def parse_detailed_description(soup: bs4.BeautifulSoup) -> interface.DetailedDescription | None:
    # Find the h2 class groupheader with text "Detailed Description"
    header = soup.find('h2', class_='groupheader',
                       string='Detailed Description')
    if not isinstance(header, bs4.element.Tag):
        return None

    div_textblock = header.find_next_sibling('div', class_='textblock')
    if not isinstance(div_textblock, bs4.element.Tag):
        raise ValueError("Expected div_textblock to be a Tag")

    desc = ""
    if fragment := div_textblock.find('pre', class_='fragment'):
        desc = fragment.get_text(strip=True)

    return interface.DetailedDescription(desc)


def parse_memitem(memitem: bs4.element.Tag):
    div_memproto = memitem.find("div", class_="memproto")  # Header
    div_memdoc = memitem.find("div", class_="memdoc")  # Description

    if not isinstance(div_memproto, bs4.element.Tag) or not isinstance(div_memdoc, bs4.element.Tag):
        raise ValueError("Expected div_memproto and div_memdoc to be Tags")

    # ================= Header =================
    td_name = div_memproto.find("td", class_="memname")
    if not td_name:
        raise ValueError("Expected to find td with class 'memname'")

    title = td_name.get_text(strip=True)
    identifier = title.partition('=')[0].rpartition('.')[-1].strip().strip('()')

    if span_mlabel := div_memproto.find("span", class_="mlabel"):
        mlabel = span_mlabel.get_text(strip=True)
        if mlabel != "static":
            raise NotImplementedError(f"mlabel '{mlabel}' not implemented")

        # TODO: handle static, flag or bool?

    # ================= Description =================

    docstring = ""
    if pre_docstring := div_memdoc.find("pre", class_="fragment"):
        docstring = pre_docstring.get_text(strip=True)

    data: list[dict] = []
    for table in div_memdoc.find_all("table", recursive=False):
        table_data = {}
        if not isinstance(table, bs4.element.Tag):
            continue

        tbody = table.find("tbody")
        if not isinstance(tbody, bs4.element.Tag):
            continue

        for tr in tbody.find_all("tr", recursive=False):
            if not isinstance(tr, bs4.element.Tag):
                continue

            tds = tr.find_all("td", recursive=False)
            if len(tds) != 2:
                raise ValueError(f"Expected 2 td elements in tr, got {len(tds)}", div_memproto)

            key = tds[0].get_text(strip=True).rstrip(':').lower()

            value_tag = tds[1]
            if not isinstance(value_tag, bs4.element.Tag):
                raise ValueError("Expected td to be a Tag")

            if key == "parameters":
                value = parse_memitem_value_parameters(value_tag)
            else:
                value = value_tag.get_text(strip=True, separator=" ")

            table_data[key] = value

        data.append(table_data)
    return interface.MemItem(title, identifier, bool(span_mlabel), docstring, data)


def parse_memitem_value_parameters(td: bs4.element.Tag) -> list[interface.Parameter]:
    if td.find("th"):  # Parameters in a table layout
        parms = []
        for tr in td.find_all("tr")[1:]:
            if not isinstance(tr, bs4.element.Tag):
                raise ValueError("Expected tr to be a Tag")
                
            tds = tr.find_all("td")
            if len(tds) < 3:
                print(td)
                raise ValueError(f"Expected at least 3 td elements in tr, got {len(tds)}")

            name = tds[0].get_text(strip=True)
            type_ = tds[1].get_text(strip=True, separator=" ")
            description = tds[2].get_text(strip=True, separator=" ")

            parms.append(interface.Parameter(name=name, type=type_, description=description))

        return parms
    
    else:  # Parameters in a single tag split by <br> tags
        for br in td.find_all("br"):
            br.replace_with(RANDOM_UUID)

        value = td.get_text(strip=True, separator=" ")

        value = [x.replace("<br>", "").strip() for x in value.split(RANDOM_UUID)]
        value = [x for x in value if x]

        parms = []
        for param_str in value:
            if '-' in param_str:
                name, _, type_ = param_str.partition('-')
                parms.append(interface.Parameter(name=name.strip(), type=type_.strip()))
            else:
                parms.append(interface.Parameter(name=param_str.strip(), type=""))

        return parms


def parse_memitems(soup: bs4.BeautifulSoup, header_text: str):
    for memitem in get_memitems(soup, header_text):
        yield parse_memitem(memitem)


def parse(page_url: str, use_cache: bool = True) -> interface.Page:
    html = cached_request.request(page_url, use_cache=use_cache)
    soup = bs4.BeautifulSoup(html, 'html.parser')

    # logging.info(f"Parsing page: {page_url}")

    detailed_desc = parse_detailed_description(soup)
    functions = list(parse_memitems(soup, "Member Function Documentation"))
    member_data = list(parse_memitems(soup, "Member Data Documentation"))
    properties = list(parse_memitems(soup, "Property Documentation"))

    return interface.Page(page_url, detailed_desc, functions, member_data, properties)
