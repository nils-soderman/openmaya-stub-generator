
import logging
import inspect
import typing
import re

from . import stub_types, utils
from .. import maya_info, documentation, resources

PROPERTY_TYPES = resources.load("property_types.jsonc")

BUILTIN_TYPES = (int, float, str, bool, tuple, list, dict)

logger = logging.getLogger(__name__)


def generate_property(name: str, prop_type: typing.Any, doc: documentation.page.Page | None) -> stub_types.Property:
    docstring = ""
    if doc:
        if doc_member := doc.find_member_by_name(name):
            if len(doc_member.data) > 0:
                docstring = doc_member.data[0].get('description', '')

    default = None
    if isinstance(prop_type, BUILTIN_TYPES) or prop_type is None:
        default = repr(prop_type)

    type_name = type(prop_type).__name__
    if prop_type is None:
        type_name = 'None'

        if default is not None:
            default += ' # type: ignore'

    return stub_types.Property(
        name=name,
        type=type_name,
        default=default,
        docstring=docstring
    )


def get_property_type_from_descriptor(desc: str) -> str:
    if " or " in desc or "," in desc:
        types = re.split(r"\s*or\s*|,\s*", desc)
        return "|".join(get_property_type_from_descriptor(t) for t in types)

    desc_processed = desc.strip()

    if desc_processed.lower().endswith(" constant"):
        return "int"  # This is an "enum" type

    if desc_processed.lower().startswith("tuple of "):
        inner_type = desc_processed[len("tuple of "):].strip()
        inner_type = inner_type.removesuffix("s")
        inner_type_name = get_property_type_from_descriptor(inner_type)
        return f"tuple[{inner_type_name}, ...]"

    type_name = utils.convert_type(desc_processed)
    return type_name


def generate_getsetter(name: str, doc: documentation.page.Page | None, custom_type: str | None) -> stub_types.PropertyGetSet:
    docstring = ""
    type_name = custom_type or "Any"
    can_set = True

    if doc:
        if doc_member := doc.find_property_by_name(name):
            if len(doc_member.data) > 0:
                docstring = doc_member.data[0].get('description', '')
                can_set = "w" in doc_member.data[0].get('access', "w").lower()

                if not custom_type:
                    type_name = doc_member.data[0].get('type', 'Any')
                    type_name = get_property_type_from_descriptor(type_name)

    return stub_types.PropertyGetSet(name,
                                     type_name,
                                     docstring=docstring,
                                     can_set=can_set)


def is_static_method(cls: type, attr_name: str) -> bool:
    val = inspect.getattr_static(cls, attr_name)
    return isinstance(val, staticmethod)


def generate_init_method(name: str, class_ref: type, method_ref: typing.Callable, doc: documentation.page.Page | None) -> list[stub_types.Method]:
    return []


def generate_method(name: str, class_ref: type, method_ref: typing.Callable, doc: documentation.page.Page | None) -> list[stub_types.Method]:
    if name == "__init__":
        return generate_init_method(name, class_ref, method_ref, doc)

    parameters = []
    docstring = None
    return_type = "Any"

    static = is_static_method(class_ref, name)

    methods = []
    if doc:
        if doc_member := doc.find_function_by_name(name):
            if doc_member.data:
                override = len(doc_member.data) > 1
                for item in doc_member.data:
                    docstring = item.get('description', '')

                    methods.append(
                        stub_types.Method(
                            name=name,
                            docstring=docstring,
                            parameters=[],
                            return_type=None,
                            static=static
                        )
                    )
            else:
                docstring = doc_member.docstring
                methods.append(
                    stub_types.Method(
                        name=name,
                        docstring=docstring,
                        parameters=[],
                        return_type=None,
                        static=static
                    )
                )

    if not methods:
        logger.warning(f"No documentation found for method {class_ref.__name__}.{name}")
        methods.append(stub_types.Method(name=name, docstring=docstring, parameters=parameters, return_type=return_type, static=static))

    return methods


def generate_class(class_ref: type, doc: documentation.page.Page | None) -> stub_types.Class:
    name = class_ref.__name__

    base_classes = [x for x in class_ref.__bases__ if x is not object]
    base_classes_names = [x.__name__ for x in base_classes]

    docstring = class_ref.__doc__ or ""

    custom_property_type_annotations = PROPERTY_TYPES.get(name, {})

    methods = []
    properties = []
    for member_name, member in class_ref.__dict__.items():
        if member_name in {'__class__', '__doc__', '__module__', '__weakref__', '__dict__', '__repr__', '__str__', '__new__'}:
            continue

        if member_name.startswith('__') and member_name.endswith('__'):
            continue # TODO: Temp, let's start by fixing the other functions first

        if (
            inspect.isfunction(member)
            or inspect.ismethod(member)
            or inspect.ismethoddescriptor(member)
            or inspect.isbuiltin(member)
        ):
            methods.extend(
                generate_method(member_name, class_ref, member, doc)
            )
        elif inspect.isgetsetdescriptor(member):
            custom_type = custom_property_type_annotations.get(member_name, {})
            properties.append(
                generate_getsetter(member_name, doc, custom_type)
            )
        # check if it's a static type
        elif isinstance(member, BUILTIN_TYPES) or member is None:
            properties.append(
                generate_property(member_name, member, doc)
            )
        else:
            properties.append(
                generate_property(member_name, member, doc)
            )

    return stub_types.Class(name=name, base_class_names=base_classes_names, docstring=docstring, methods=methods, properties=properties)


def generate_classes(module: str, doc_index: documentation.index.Index | None, use_cache: bool) -> list[stub_types.Class]:
    class_references = maya_info.get_classes(module)
    if not class_references:
        return []

    classes: list[stub_types.Class] = []

    for class_ref in class_references:
        if class_ref is object:
            continue

        doc_page = None
        if doc_index:
            if doc_class := doc_index.get_class_by_name(class_ref.__name__):
                doc_page = documentation.parse(doc_class.url, use_cache)

        classes.append(generate_class(class_ref, doc_page))

    return classes
