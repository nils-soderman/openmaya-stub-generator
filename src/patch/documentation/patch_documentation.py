"""
Patch stubs based on the Online Documentation
"""

from ...stub_types import Class, Property, PropertyGetSet
from ...flags import Flags

from ..base import PatchBase

from . import parser, convert_type


def is_none_or_any(s: str | None) -> bool:
    return s is None or s == "Any"


class Patch_Documentation(PatchBase):
    ORDER = 5

    def __init__(self, module_name: str, version: int, flags: Flags) -> None:
        super().__init__(module_name, version, flags)

        self.use_cache = bool(flags & Flags.CACHE)

        api2 = "api" in module_name

        self.parser = parser.get_parser(api2, self.use_cache)
        self.index = None
        if namespace := self.parser.get_namespace(module_name, version):
            self.index = self.parser.get_index(namespace)

    def patch_class(self, class_: Class):
        if not self.index:
            return

        doc_index_entry = self.index.get_class_by_name(class_.name)
        if not doc_index_entry:
            return

        class_doc = self.parser.parse_class_page(doc_index_entry.url)

        for property in class_.properties:
            if prop_doc := class_doc.find_property_by_name(property.name):
                self.patch_property(property, prop_doc)

    def patch_property(self, property_: Property, prop_doc: parser.interface.MemItem):
        if is_none_or_any(property_.type) and len(prop_doc.data) > 0:
            if len(prop_doc.data) > 1:
                raise NotImplementedError("Multiple types in documentation not supported yet")

            data = prop_doc.data[0]

            if type_desc := data.get('type'):
                property_.type = convert_type.get_python_type_from_desc(type_desc)

            if isinstance(property_, PropertyGetSet):
                # read/write access is documented as a 1-2 letter string
                # For example: Access: "RW"
                access = data.get('access', "RW").lower()
                property_.can_set = "w" in access
