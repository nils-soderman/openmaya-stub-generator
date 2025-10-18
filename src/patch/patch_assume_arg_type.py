""" 
Static methods cannot return 'Self', make them return the class instead
"""
import re

from .base import PatchBase


PRIMITIVE_TYPES = {"int", "float", "str", "bool", "list", "dict", "set", "tuple"}

TYPE_CONVERSION_MAPPING = {
    "short": "int"
}

PATTERNS = (
    (re.compile(r".*name$"), "str"),
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

    def patch_method(self, class_, method):
        if method.parameters:
            for param in method.parameters:
                if param.type and param.type != "Any":
                    continue

                if type_ := get_type_from_name(param.name):
                    param.type = type_
