""" 
Make sure argument names are safe for use in Python code
"""
import keyword

from .base import PatchBase

DISSALLOWED_NAMES = set(keyword.kwlist)

DISSALLOWED_CHARS = set("!@#$%^&()-+=[]{}|;:'\",.<>?/\\`~ ")


class Patch_SafeParameterName(PatchBase):
    def desc(self) -> str:
        return "Make sure parameter names are sanitized and safe for use in Python code"

    def patch_method(self, class_, method):
        taken_names = set()
        if method.parameters:
            for parameter in method.parameters:
                if parameter.name in DISSALLOWED_NAMES:
                    parameter.name += "_"

                if "*" in parameter.name and parameter.name not in {"*args", "**kwargs"}:
                    parameter.name = f"arg"

                if any(char in DISSALLOWED_CHARS for char in parameter.name):
                    parameter.name = "arg"

                # Make sure there are no duplicate names
                if parameter.name in taken_names:
                    i = 1
                    new_name = parameter.name
                    while new_name in taken_names:
                        i += 1
                        new_name = f"{parameter.name}{i}"
                    parameter.name = new_name

                taken_names.add(parameter.name)
