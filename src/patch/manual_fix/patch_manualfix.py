""" 
Insert manually typed documentation into stubs
"""

from ..base import PatchBase
from . import resources


class Patch_ManualFix(PatchBase):
    ORDER = 500

    def __init__(self, module_name, version, flags) -> None:
        super().__init__(module_name, version, flags)

        self.property_types: dict[str, dict[str, str]] = resources.load_module_resource(module_name, "property_type.jsonc")

    def patch_property(self, class_, property_):
        if class_info := self.property_types.get(class_.name):
            if type_ := class_info.get(property_.name):
                property_.type = type_
