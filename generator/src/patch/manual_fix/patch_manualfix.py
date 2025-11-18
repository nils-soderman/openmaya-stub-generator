""" 
Insert manually typed documentation into stubs
"""

from ...stub_types import Class, Method
from ..base import PatchBase
from . import resources


class Patch_ManualFix(PatchBase):
    ORDER = 500

    def __init__(self, module_name, version, flags) -> None:
        super().__init__(module_name, version, flags)

        self.property_types: dict[str, dict[str, str]] = resources.load_module_resource(module_name, "property_type.jsonc")
        self.method_arg_types: dict[str, dict[str, dict[str, str]]] = resources.load_module_resource(module_name, "method_arg_type.jsonc")
        self.method_return_types: dict[str, dict[str, str]] = resources.load_module_resource(module_name, "method_return_type.jsonc")

        self.method_arg_defaults: dict[str, dict[str, dict[str, str]]] = resources.load_module_resource(module_name, "method_arg_default.jsonc")

    def patch_property(self, class_, property_):
        if class_info := self.property_types.get(class_.name):
            if type_ := class_info.get(property_.name):
                property_.type = type_

    def patch_method(self, class_: Class, method: Method, overload: Method | None = None):
        if arg_types_info := self.method_arg_types.get(class_.name):
            if method_info := arg_types_info.get(method.name):
                if method.parameters:
                    for param in method.parameters:
                        if param_type := method_info.get(param.name):
                            param.type = param_type

        if arg_defaults_info := self.method_arg_defaults.get(class_.name):
            if method_info := arg_defaults_info.get(method.name):
                if method.parameters:
                    for param in method.parameters:
                        if param_default := method_info.get(param.name):
                            param.default = param_default

        if return_types_info := self.method_return_types.get(class_.name):
            if return_type := return_types_info.get(method.name):
                method.return_type = return_type
