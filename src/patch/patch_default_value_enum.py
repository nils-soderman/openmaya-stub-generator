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
        self.current_module = importlib.import_module(module_name)

    def patch_method(self, class_, method, overload=None):
        if method.parameters:
            for param in method.parameters:
                if param.default:
                    if re.match(r'^k[A-Z]', param.default) or re.search(r'\.k[A-Z]', param.default):
                        if enum_class := find_enum_class((self.current_module, self.main_module), param.default):
                            param.type = type(getattr(enum_class, param.default)).__name__
                            param.default = f"{enum_class.__name__}.{param.default}"
                        
                        elif "." in param.default:
                            class_name, _, enum_name = param.default.rpartition(".")
                            if hasattr(self.current_module, class_name):
                                cls = getattr(self.current_module, class_name)
                                if hasattr(cls, enum_name):
                                    param.type = type(getattr(cls, enum_name)).__name__

                            elif hasattr(self.main_module, class_name):
                                cls = getattr(self.main_module, class_name)
                                if hasattr(cls, enum_name):
                                    param.type = type(getattr(cls, enum_name)).__name__
