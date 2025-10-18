""" 
Make sure argument names are safe for use in Python code
"""

from .base import PatchBase
from ..stub_types import Parameter

RETURN_TYPES = {
    "__init__": "None",
    "__len__": "int",
    "__ge__": "bool",
    "__gt__": "bool",
    "__le__": "bool",
    "__lt__": "bool",
    "__eq__": "bool",
    "__ne__": "bool",
    "__delitem__": "None",
    "__setitem__": "None",
    "__contains__": "bool",
    "append": "None",
    "clear": "None",
    "insert": "None",
    "remove": "None",
}

PARAMETERS = {
    "__len__": [],
    "__iter__": [],
    "__next__": [],
    "__ge__": ["other"],
    "__gt__": ["other"],
    "__le__": ["other"],
    "__lt__": ["other"],
    "__eq__": ["other"],
    "__ne__": ["other"],
    "__add__": ["other"],
    "__sub__": ["other"],
    "__mul__": ["other"],
    "__truediv__": ["other"],
    "__floordiv__": ["other"],
    "__mod__": ["other"],
    "__pow__": ["other"],
    "__rmul__": ["other"],
    "__iadd__": ["other"],
    "__imul__": ["other"],
    "__rtruediv__": ["other"],
    "__itruediv__": ["other"],
    "__getitem__": ["index: int"],
    "__setitem__": ["index: int", "value"],
    "__delitem__": ["index: int"],
    "__contains__": ["item"],
    "append": ["item"],
    "clear": [],
    "insert": ["index: int", "item"],
    "remove": ["item"],
}


class Patch_BuiltinMethods(PatchBase):
    ORDER = 1

    def patch_method(self, class_, method):
        if method.name in RETURN_TYPES:
            method.return_type = RETURN_TYPES[method.name]

        if method.name in PARAMETERS:
            method.parameters = []
            for param_str in PARAMETERS[method.name]:
                name, _, type_ = param_str.partition(":")
                name = name.strip()
                type_ = type_.strip()

                method.parameters.append(
                    Parameter(name=name, type=type_ or None)
                )
