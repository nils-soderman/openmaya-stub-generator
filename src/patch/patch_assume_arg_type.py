""" 
Static methods cannot return 'Self', make them return the class instead
"""
import re

from src.stub_types import Class, Property

from .base import PatchBase


PRIMITIVE_TYPES = {"int", "float", "str", "bool", "list", "dict", "set", "tuple"}

TYPE_CONVERSION_MAPPING = {
    "short": "int",
    "function": "Callable",
}

PATTERNS = (
    (re.compile(r".*name$"), "str"),
)

PROPERTY_PATTERNS = (
    (re.compile(r"Name$"), "str"),
)


def get_type_from_name(name: str) -> str | None:
    if name in PRIMITIVE_TYPES:
        return name

    if name in TYPE_CONVERSION_MAPPING:
        return TYPE_CONVERSION_MAPPING[name]

    for pattern, type_ in PATTERNS:
        if pattern.match(name, re.IGNORECASE):
            return type_

    return None


class Patch_AssumeParameterType(PatchBase):
    ORDER = 50

    def patch_property(self, class_: Class, property: Property):
        if property.type and property.type != "Any":
            return

        for pattern, type_ in PROPERTY_PATTERNS:
            if pattern.match(property.name, re.IGNORECASE):
                property.type = type_
                return

    def patch_method(self, class_, method, overload=None):
        if method.parameters:
            for param in method.parameters:
                if param.type and param.type != "Any":
                    continue

                if type_ := get_type_from_name(param.name):
                    param.type = type_
