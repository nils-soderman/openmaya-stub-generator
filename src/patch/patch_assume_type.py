""" 
Assume parameter types based on their names
"""
import re

from src.stub_types import Class, Property

from .base import PatchBase

MAYA_OBJ_PATTERN = re.compile(r"^M[A-Z].*")

PRIMITIVE_TYPES = {"int", "float", "str", "bool", "list", "dict", "set", "tuple"}

TYPE_CONVERSION_MAPPING = {
    "function": "Callable",

    "string": "str",
    "text": "str",

    "index": "int",
    "long": "int",
    "short": "int",
}

PATTERNS = (
    (re.compile(r".*name$", re.IGNORECASE), "str"),
    (re.compile(r"[A-z]+Count$"), "int"),
    (re.compile(r"[A-z]+Index$"), "int"),
    (re.compile(r"^num[A-z]"), "int"),
    (re.compile(r"^is[A-Z0-9]"), "bool"),
)

PROPERTY_PATTERNS = (
    (re.compile(r"^enforce"), "bool"),
    (re.compile(r".*Name$"), "str"),
    (re.compile(r"^is[A-Z0-9]"), "bool"),
    (re.compile(f"^use[A-Z]"), "bool"),
    (re.compile(r"^enable[A-Z0-9]"), "bool"),
    (re.compile(r".*Enabled$"), "bool"),
    (re.compile(f".*[A-z]Type$"), "int"),
    (re.compile(f".*Distance$"), "float"),
    (re.compile(f".*Length$"), "float"),
)


def get_type_from_name(name: str) -> str | None:
    if name in PRIMITIVE_TYPES:
        return name

    if name in TYPE_CONVERSION_MAPPING:
        return TYPE_CONVERSION_MAPPING[name]

    for pattern, type_ in PATTERNS:
        if pattern.match(name):
            return type_

    return None


def get_type_from_default_value(default_value: str | None) -> str | None:
    if default_value is None:
        return None

    if default_value.isdigit():
        return "int"
    try:
        float(default_value)
        return "float"
    except ValueError:
        pass

    if default_value.startswith(("'", '"')) and default_value.endswith(("'", '"')):
        return "str"

    if default_value in ("True", "False"):
        return "bool"

    return None


class Patch_AssumeTypes(PatchBase):
    ORDER = 50

    def patch_property(self, class_: Class, property: Property):
        if property.type and property.type != "Any":
            return

        for pattern, type_ in PROPERTY_PATTERNS:
            if pattern.match(property.name):
                property.type = type_
                return

    def patch_method(self, class_, method, overload=None):
        if method.parameters:
            for param in method.parameters:
                if param.type and param.type != "Any":
                    continue

                if type_ := get_type_from_name(param.name):
                    param.type = type_

                elif type_ := get_type_from_default_value(param.default):
                    param.type = type_

                elif MAYA_OBJ_PATTERN.match(param.name):
                    param.type = param.name
                    param.name = param.name[1:]  # Remove leading 'M'
