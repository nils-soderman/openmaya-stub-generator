"""
Make sure argument names are safe for use in Python code
"""

import importlib
import inspect
import typing
import types
import re

from src.flags import Flags
from .base import PatchBase


def find_enum_class(modules: typing.Sequence[types.ModuleType], enum_name: str) -> type | None:
    """
    Find the class that contains the enum value
    """
    for module in modules:
        for name, obj in inspect.getmembers(module, inspect.isclass):
            if hasattr(obj, enum_name):
                return obj
    return None


class Patch_DefaultValueEnum(PatchBase):
    ORDER = 500

    def __init__(self, module_name: str, version: int, flags: Flags) -> None:
        main_module_name = "maya.api.OpenMaya" if "api" in module_name else "maya.OpenMaya"
        self.main_module = importlib.import_module(main_module_name)
        self.current_module = importlib.import_module(f"maya.{module_name}")

    def patch_method(self, class_, method, overload=None):

        if method.parameters:
            for param in method.parameters:
                if param.default and re.match(r'^k[A-Z]', param.default):
                    # Default value is a enum value, we need to append the correct class in front "kValue" -> "ClassName.kValue"
                    if enum_class := find_enum_class((self.current_module, self.main_module), param.default):
                        param.default = f"{enum_class.__name__}.{param.default}"
