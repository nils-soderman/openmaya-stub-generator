"""
Patch stubs based on the Online Documentation
"""
import contextlib

from ...stub_types import Class, Parameter, Property, PropertyGetSet, Method
from ...flags import Flags

from ..base import PatchBase

from . import parser, convert_type, operator_overloads
from .parser import signature


def is_none_or_any(s: str | None) -> bool:
    return s is None or s == "Any"


def sanitize_default_value(default: str | None) -> str | None:
    """
    Sanitize default value strings extracted from documentation
    """
    if default is None:
        return None

    default = default.strip()
    if default.lower() in ("none", "null"):
        return "None"

    return default


class Patch_Documentation(PatchBase):
    ORDER = 5

    def __init__(self, module_name: str, version: int, flags: Flags) -> None:
        super().__init__(module_name, version, flags)

        self.use_cache = bool(flags & Flags.CACHE)

        api2 = "api" in module_name

        self.index = None
        self.parser = None
        with contextlib.suppress(NotImplementedError):
            self.parser = parser.get_parser(api2, self.use_cache)
            if namespace := self.parser.get_namespace(module_name.rpartition('.')[-1], version):
                self.index = self.parser.get_index(namespace)

        convert_type.g_current_module_name = module_name

    def is_valid(self) -> bool:
        return self.index is not None

    def patch_class(self, class_: Class):
        if not self.index or self.parser is None:
            return

        doc_index_entry = self.index.get_class_by_name(class_.name)
        if not doc_index_entry:
            return

        class_doc = self.parser.parse_class_page(doc_index_entry.url)

        for property in class_.properties:
            if prop_doc := class_doc.find_property_by_name(property.name):
                self.patch_property(class_, property, prop_doc)

        for method in class_.methods:
            if method.name.startswith("__") and method.name.endswith("__"):
                self.patch_builtin_method(class_, method, class_doc)
            elif method_doc := class_doc.find_function_by_name(method.name):
                self.patch_method(class_, method, method_doc)

    def patch_property(self, class_: Class, property_: Property, prop_doc: parser.interface.MemItem):
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

    def patch_init_method(self, class_: Class, method: Method, class_doc: parser.interface.Page):
        if class_doc.detailed_description and class_doc.detailed_description.constructors:
            for i, constructor in enumerate(class_doc.detailed_description.constructors):
                if i > 0:
                    # Create a new overload method
                    new_method = Method(method.ref,
                                        method.name,
                                        return_type="None",
                                        docstring=method.docstring,
                                        deprecated=method.deprecated,
                                        static=method.static)
                    method.overloads.append(new_method)
                else:
                    new_method = method

                new_method.docstring = constructor.description
                new_method.return_type = "None"
                new_method.parameters = []

                signature_info = signature.parse_signature(constructor.signature)

                for param in constructor.parameters:
                    if " - " in param:
                        param_name, _, param_type_desc = param.partition(" - ")
                        param_type = convert_type.get_python_type_from_desc(param_type_desc)
                    else:
                        param_name = param
                        param_type = "Any"

                    default_value = None
                    signature_info_param = next((x for x in signature_info.parameters if x.name == param_name), None)
                    if signature_info_param and signature_info_param.default:
                        default_value = sanitize_default_value(signature_info_param.default)

                    new_method.parameters.append(
                        Parameter(
                            name=param_name,
                            type=param_type,
                            default=default_value
                        )
                    )
        elif class_.docstring:
            for i, signature_str in enumerate(signature.extract_signatures_from_docstring(class_.docstring, method.name, stop_search_at_text=False)):
                signature_info = signature.parse_signature(signature_str)
                if i > 0:
                    # Create a new overload method
                    new_method = Method(method.ref,
                                        method.name,
                                        return_type="None",
                                        docstring=method.docstring,
                                        deprecated=method.deprecated,
                                        static=method.static)
                    method.overloads.append(new_method)
                else:
                    new_method = method

                new_method.deprecated = signature_info.is_obsolete
                new_method.return_type = "None"
                new_method.parameters = []

                before, _, after = class_.docstring.partition(signature_str.strip())
                if after:
                    new_method.docstring = after.partition('\n\n')[0].strip()

                for param in signature_info.parameters:
                    if param.param_type:
                        param_type = convert_type.get_python_type_from_desc(param.param_type)
                    else:
                        param_type = "Any"

                    new_method.parameters.append(
                        Parameter(
                            name=param.name,
                            type=param_type,
                            default=sanitize_default_value(param.default),
                        )
                    )

    def patch_builtin_method(self, class_: Class, method: Method, class_doc: parser.interface.Page):
        if method.name == "__init__":
            return self.patch_init_method(class_, method, class_doc)

        operator_overloads.process_operator_overloads(class_, method, class_doc)

    def patch_method(self, class_: Class, method: Method, method_doc: parser.interface.MemItem):
        if method_doc.data:
            self.patch_method_from_data(method, method_doc)
        else:
            self.patch_method_from_docstring_signatures(method, method_doc.docstring)

    def patch_method_from_data(self, in_method: Method, method_doc: parser.interface.MemItem):
        """
        If method is properly documented, patch based on the parsed data
        """
        for i, data in enumerate(method_doc.data):
            if i > 0:
                # Create a new overload method
                method = Method(in_method.ref,
                                in_method.name,
                                return_type="Any",
                                docstring=in_method.docstring,
                                deprecated=in_method.deprecated,
                                static=in_method.static)
                in_method.overloads.append(method)
            else:
                method = in_method

            if docstring := data.get('description'):
                method.docstring = docstring

            signature_info = None
            signature_str = data.get('signature') or data.get('name')
            if signature_str:
                signature_info = signature.parse_signature(signature_str)

            method.parameters = []

            params_info = data.get('parameters', [])

            # Check if the params is documented as "None."
            # If so empty the params list
            if len(params_info) == 1:
                first_param_info = params_info[0]
                if isinstance(first_param_info, parser.interface.Parameter):
                    param_name_lower = first_param_info.name.lower()
                    if param_name_lower.strip(".") == "none" and not first_param_info.type:
                        params_info = []

            for i, param_doc in enumerate(params_info):
                if not isinstance(param_doc, parser.interface.Parameter):
                    raise TypeError("Expected Parameter instance")

                default = param_doc.default
                if signature_info:
                    if not default and i < len(signature_info.parameters):
                        default = signature_info.parameters[i].default

                if default:
                    default = default.replace(" ", "")

                method.parameters.append(
                    Parameter(
                        name=param_doc.name,
                        type=convert_type.get_python_type_from_desc(param_doc.type),
                        default=sanitize_default_value(default),
                    )
                )

            # Return type
            if return_type_desc := data.get('returns'):
                method.return_type = convert_type.get_python_type_from_desc(return_type_desc)

    def patch_method_from_docstring_signatures(self, in_method: Method, desc: str):
        """
        Some methods are not properly documented, and only have a docstring with signatures.
        Try to extract type information from those signatures.
        """
        signature_strs = signature.extract_signatures_from_docstring(desc, in_method.name)
        for index, signature_str in enumerate(signature_strs):
            signature_info = signature.parse_signature(signature_str)
            if index > 0:
                # Create a new overload method
                method = Method(in_method.ref,
                                in_method.name,
                                return_type="Any",
                                docstring=in_method.docstring,
                                deprecated=in_method.deprecated,
                                static=in_method.static)
                in_method.overloads.append(method)
            else:
                method = in_method

            method.deprecated = signature_info.is_obsolete

            method.return_type = convert_type.get_python_type_from_desc(signature_info.return_type or "None")

            method.parameters = []
            for param in signature_info.parameters:
                if param.param_type:
                    param_type = convert_type.get_python_type_from_desc(param.param_type)
                else:
                    param_type = "Any"

                if is_none_or_any(param_type):
                    if new_type := signature.extract_param_type_from_docstring(param.name, desc):
                        param_type = convert_type.get_python_type_from_desc(new_type)

                default = None
                if param.default:
                    if ":" in param.default:
                        default = "..."
                    else:
                        default = param.default

                method.parameters.append(
                    Parameter(
                        name=param.name,
                        type=param_type,
                        default=sanitize_default_value(default),
                    )
                )
