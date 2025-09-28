import typing

import dataclasses
import requests
import logging
import bs4

from . import cached_request

logger = logging.getLogger(__name__)


class MemItem(typing.NamedTuple):
    title: str
    identifier: str
    is_static: bool
    docstring: str
    data: list[dict]


class DetailedDescription(typing.NamedTuple):
    description: str


@dataclasses.dataclass
class Page:
    url: str
    detailed_description: DetailedDescription | None
    functions: list[MemItem]
    member_data: list[MemItem]
    properties: list[MemItem]

    def find_member_by_name(self, name: str) -> MemItem | None:
        for member in self.member_data:
            if member.identifier == name:
                return member
        return None
    
    def find_property_by_name(self, name: str) -> MemItem | None:
        for prop in self.properties:
            if prop.identifier == name:
                return prop
        return None
    
    def find_function_by_name(self, name: str) -> MemItem | None:
        for func in self.functions:
            if func.identifier == name:
                return func
        return None


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


def parse_detailed_description(soup: bs4.BeautifulSoup) -> DetailedDescription | None:
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

    return DetailedDescription(desc)


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
            value = tds[1].get_text(strip=True, separator=" ")
            table_data[key] = value

        data.append(table_data)
    return MemItem(title, identifier, bool(span_mlabel), docstring, data)


def parse_memitems(soup: bs4.BeautifulSoup, header_text: str):
    for memitem in get_memitems(soup, header_text):
        yield parse_memitem(memitem)


def parse(page_url: str, use_cache: bool = True) -> Page:
    if use_cache:
        html = cached_request.request(page_url, use_cache=True)
    else:
        response = requests.get(page_url)
        response.raise_for_status()
        html = response.text
    soup = bs4.BeautifulSoup(html, 'html.parser')

    logging.info(f"Parsing page: {page_url}")

    detailed_desc = parse_detailed_description(soup)
    functions = list(parse_memitems(soup, "Member Function Documentation"))
    member_data = list(parse_memitems(soup, "Member Data Documentation"))
    properties = list(parse_memitems(soup, "Property Documentation"))

    return Page(page_url, detailed_desc, functions, member_data, properties)
