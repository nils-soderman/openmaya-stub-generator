import typing
import json

import bs4

from .. import cached_request, interface

AUTODESK_HELP_BASE_URL = "https://help.autodesk.com/cloudhelp"
AUTODESK_MAYA_API_NAMESPACE_PATH = "/ENU/MAYA-API-REF/py_ref"


def get_base_url(version: int) -> str:
    return f"{AUTODESK_HELP_BASE_URL}/{version}{AUTODESK_MAYA_API_NAMESPACE_PATH}"


def get_namespaces(version: int, use_cache: bool) -> list[interface.Namespace]:
    base_url = get_base_url(version)
    url = f"{base_url}/namespaces.js"
    js_raw = cached_request.request(url, use_cache=use_cache)

    js_parsable = js_raw.replace(
        "var namespaces =", "").strip().rstrip(";")

    namespace_content: list = json.loads(js_parsable)

    return [interface.Namespace(x[0], version, f"{base_url}/{x[1]}") for x in namespace_content]


def find_table_by_heading(tables: list[bs4.element.Tag], heading: str):
    for table in tables:
        if heading_row := table.find('tr', class_='heading'):
            heading_text = heading_row.get_text(strip=True)

            if heading.lower() == heading_text.lower():
                return table

    return None


def parse_table_url(table: bs4.element.Tag, base_url: str) -> typing.Generator[interface.IndexClass, None, None]:
    for a_tag in table.find_all('a'):
        if not isinstance(a_tag, bs4.element.Tag):
            raise ValueError("Expected a_tag to be a Tag")

        class_name = a_tag.get_text(strip=True)
        class_url = str(a_tag.get('href', ''))

        if class_name and class_url:
            yield interface.IndexClass(class_name, f"{base_url}/{class_url}")


def parse_table_functions(table: bs4.element.Tag, base_url: str) -> typing.Generator[interface.IndexFunction, None, None]:
    for a_tag in table.find_all('a'):
        if not isinstance(a_tag, bs4.element.Tag):
            raise ValueError("Expected a_tag to be a Tag")

        class_name = a_tag.get_text(strip=True)
        class_url = str(a_tag.get('href', ''))

        if class_name and class_url:
            yield interface.IndexFunction(class_name, f"{base_url}/{class_url}")


def parse_table_variables(table: bs4.element.Tag) -> typing.Generator[interface.IndexVariable, None, None]:
    # Find all tr elements and filter by class starting with "memitem:"
    for row in table.find_all('tr'):
        if not isinstance(row, bs4.element.Tag):
            continue

        # Check if any class starts with "memitem:"
        row_classes = row.get('class')
        if not row_classes:
            continue

        # row_classes can be a string or list of strings
        if isinstance(row_classes, str):
            class_list = [row_classes]
        else:
            class_list = row_classes

        if not any(cls.startswith('memitem:') for cls in class_list):
            continue

        cols = row.find_all('td')
        if len(cols) < 2:
            continue

        type_col = cols[0].get_text(strip=True)
        name_col = cols[1].get_text(strip=True)

        if '=' in name_col:
            name, default = map(str.strip, name_col.split('=', 1))
        else:
            name, default = name_col, None

        if name and type_col:
            yield interface.IndexVariable(name, type_col, default)


def get_namespace_index(namespace: interface.Namespace, use_cache: bool) -> interface.Index:
    html = cached_request.request(namespace.url, use_cache=use_cache)

    soup = bs4.BeautifulSoup(html, 'html.parser')

    contents_div = soup.find('div', class_='contents')

    if not isinstance(contents_div, bs4.element.Tag):
        raise ValueError("Could not find contents div")

    member_tables = contents_div.find_all('table', class_='memberdecls')
    member_tables = [
        x for x in member_tables if isinstance(x, bs4.element.Tag)]

    classes = []
    functions = []
    variables = []

    base_url = namespace.url.rpartition('/')[0]

    if table_classes := find_table_by_heading(member_tables, "Classes"):
        classes = list(parse_table_url(table_classes, base_url))

    if table_functions := find_table_by_heading(member_tables, "Functions"):
        functions = list(parse_table_functions(table_functions, base_url))

    if table_variables := find_table_by_heading(member_tables, "Variables"):
        variables = list(parse_table_variables(table_variables))

    return interface.Index(classes, functions, variables)
