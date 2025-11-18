""" 
Make sure Maya objects have their correct module prefixes
E.g. "MObject" -> "om.MObject" if outside of "OpenMaya" module. 
"""

from .base import PatchBase
from .documentation import convert_type


class Patch_MayaTypes(PatchBase):
    def __init__(self, module_name, version, flags) -> None:
        super().__init__(module_name, version, flags)

        convert_type.g_current_module_name = module_name

    def patch_class(self, class_):
        super().patch_class(class_)
        for i, base_class in enumerate(class_.base_class_names):
            base_class = convert_type.add_maya_module_prefix(base_class)
            class_.base_class_names[i] = base_class

    def patch_property(self, class_, property):
        property.type = convert_type.add_maya_module_prefix(property.type)

    def patch_method(self, class_, method, overload=None):
        super().patch_method(class_, method, overload)
        if method.parameters:
            for parameter in method.parameters:
                if parameter.type:
                    parameter.type = convert_type.add_maya_module_prefix(parameter.type)

                if parameter.default:
                    converted_type = convert_type.add_maya_module_prefix(parameter.default)
                    if converted_type == "Any":
                        converted_type = "..."
                    parameter.default = converted_type
