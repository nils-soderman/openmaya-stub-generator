import dataclasses
import typing


# =========================================================
# region                   INDEX
# =========================================================

class Namespace(typing.NamedTuple):
    name: str
    version: int
    url: str


class IndexClass(typing.NamedTuple):
    name: str
    url: str


class IndexFunction(typing.NamedTuple):
    name: str
    url: str


class IndexVariable(typing.NamedTuple):
    name: str
    type: str
    default: str | None = None


@dataclasses.dataclass
class Index:
    classes: list[IndexClass]
    functions: list[IndexFunction]
    variables: list[IndexVariable]

    def get_class_by_name(self, name: str) -> IndexClass | None:
        for cls in self.classes:
            if cls.name == name:
                return cls
        return None

    def get_function_by_name(self, name: str) -> IndexFunction | None:
        for func in self.functions:
            if func.name == name:
                return func
        return None

    def get_variable_by_name(self, name: str) -> IndexVariable | None:
        for var in self.variables:
            if var.name == name:
                return var
        return None


# =========================================================
# region                CLASS PAGE
# =========================================================

class MemItem(typing.NamedTuple):
    title: str
    identifier: str
    is_static: bool
    docstring: str
    data: list[dict]


class Parameter(typing.NamedTuple):
    name: str
    type: str
    default: str | None = None
    description: str = ""

class DetailedDescription(typing.NamedTuple):
    description: str


@dataclasses.dataclass
class Page:
    url: str
    detailed_description: str | None
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


# =========================================================
# region                PARSER BASE
# =========================================================

class ParserBase:
    def __init__(self, use_cache: bool) -> None:
        self.use_cache = use_cache

    def get_namespaces(self, version: int) -> list[Namespace]:
        raise NotImplementedError

    def get_namespace(self, namespace: str, version: int) -> Namespace | None:
        return next((x for x in self.get_namespaces(version) if x.name == namespace), None)

    def get_index(self, namespace: Namespace) -> Index:
        raise NotImplementedError

    def parse_class_page(self, url: str) -> Page:
        raise NotImplementedError
