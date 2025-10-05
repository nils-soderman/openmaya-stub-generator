import logging
import inspect
import typing
import re

from . import stub_types, utils
from .. import maya_info, documentation, resources

PROPERTY_TYPES = resources.load("property_types.jsonc")

BUILTIN_TYPES = (int, float, str, bool, tuple, list, dict)

logger = logging.getLogger(__name__)


class MethodSignature(typing.NamedTuple):
    docstring: str | None
    return_type: str | None = "Any"
    parameters: list[stub_types.Parameter] = []


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
    desc = re.sub(r'<[^>]+>', '', desc)  # Remove HTML tags that may be left if the online docs html is broken
    desc = desc.strip()

    bracket_list_pattern = r'(?<!list)\[([^\[\]]+)\]'
    if re.search(bracket_list_pattern, desc):
        def __replace_bracket_list(match):
            inner_content = match.group(1)
            types = []
            for x in inner_content.split(','):
                if x.strip() == "...":
                    continue
                converted_type = get_property_type_from_descriptor(x)
                if converted_type not in types:
                    types.append(converted_type)

            return f"list[{'|'.join(types)}]"

        # Replace all bracket lists with their converted form
        desc = re.sub(bracket_list_pattern, __replace_bracket_list, desc)

    if " or " in desc:
        types = re.split(r"\sor\s|,\s*", desc)
        return "|".join(get_property_type_from_descriptor(t) for t in types)
    
    if "/" in desc:
        types = desc.split("/")
        return "|".join(get_property_type_from_descriptor(t) for t in types)

    if desc.startswith("(") and desc.endswith(")"):
        types = desc[1:-1].split(",")
        all_types = ",".join(get_property_type_from_descriptor(t) for t in types)
        return f"tuple[{all_types}]"

    desc_processed = desc.strip()
    if desc_processed.lower().endswith("."):
        desc_processed = desc_processed[:-1].strip()

    if desc_processed.lower().startswith("the new "):
        desc_processed = desc_processed[len("the new "):].strip()

    if desc_processed.lower().endswith(" constant"):
        return "int"  # This is an "enum" type

    if desc_processed.lower().startswith("tuple of "):
        inner_type = desc_processed[len("tuple of "):].strip()
        inner_type = inner_type.removesuffix("s")
        inner_type_name = get_property_type_from_descriptor(inner_type)
        return f"tuple[{inner_type_name}, ...]"

    if desc_processed.lower().startswith("list of "):
        inner_type = desc_processed[len("list of "):].strip()
        inner_type = inner_type.removesuffix("s")
        inner_type_name = get_property_type_from_descriptor(inner_type)
        return f"list[{inner_type_name}]"

    if desc_processed.lower().endswith("reference to self"):
        return "Self"

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


def patch_default(value: str) -> str:
    if value == "none":
        return "None"

    return value


def get_method_signature(method_ref: typing.Callable, doc_member: documentation.page.MemItem):
    if doc_member.data:
        for item in doc_member.data:
            docstring = item.get('description', '')

            parameters: list[stub_types.Parameter] = []
            
            doc_params: list[documentation.page.Parameter] = item.get('parameters', [])
            signature = item.get('signature') or item.get('name')
            if signature:
                signature_params, sig_return_type = documentation.post.parse_signature(signature)
                for signature_param in signature_params:
                    default = signature_param.default
                    if default:
                        default = patch_default(default)

                    type_ = None
                    if x := next((x for x in doc_params if x.name == signature_param.name), None):
                        if x.type:
                            type_ = get_property_type_from_descriptor(x.type)
                    if not type_ and signature_param.param_type:
                        type_ = get_property_type_from_descriptor(signature_param.param_type)

                    parameters.append(
                        stub_types.Parameter(name=signature_param.name, type=type_, default=default)
                    )

            if return_type := item.get('returns'):
                return_type = get_property_type_from_descriptor(return_type)
            else:
                return_type = "Any"

            yield MethodSignature(
                docstring=docstring,
                parameters=parameters,
                return_type=return_type
            )

    else:
        # First line of the docstring should be the signature
        signatures = documentation.post.extract_signature_from_docstring(doc_member.docstring, doc_member.identifier)
        if signatures:
            for signature in signatures:
                signature_params, sig_return_type = documentation.post.parse_signature(signature)

                parameters = []
                for param in signature_params:
                    default = param.default
                    if default:
                        default = patch_default(default)

                    param_type = None
                    if param.param_type:
                        param_type = get_property_type_from_descriptor(param.param_type)
                    else:
                        # Try to get the type from the docstring
                        if param_type := documentation.post.extract_parameter_types_from_docstring(param.name, doc_member.docstring):
                            param_type = get_property_type_from_descriptor(param_type)

                    parameters.append(
                        stub_types.Parameter(name=param.name, type=param_type, default=default)
                    )

                return_type = get_property_type_from_descriptor(sig_return_type) if sig_return_type else "Any"

                yield MethodSignature(
                    docstring=doc_member.docstring,
                    parameters=parameters,
                    return_type=return_type
                )
        else:
            logger.warning(f"Method {doc_member.identifier} has no signature in the documentation!")

            yield MethodSignature(
                docstring=doc_member.docstring,
                parameters=[
                    stub_types.Parameter(name="*args", type=None),
                    stub_types.Parameter(name="**kwargs", type=None)
                ]
            )


def generate_method(name: str, class_ref: type, method_ref: typing.Callable, doc: documentation.page.Page | None) -> list[stub_types.Method]:
    if name == "__init__":
        return generate_init_method(name, class_ref, method_ref, doc)

    static = is_static_method(class_ref, name)

    methods = []
    if doc:
        if doc_member := doc.find_function_by_name(name):
            for signature in get_method_signature(method_ref, doc_member):
                methods.append(
                    stub_types.Method(
                        name=name,
                        docstring=signature.docstring,
                        parameters=signature.parameters,
                        return_type=signature.return_type,
                        static=static
                    )
                )

    if not methods:
        logger.warning(f"No documentation found for method {class_ref.__name__}.{name}")
        methods.append(
            stub_types.Method(
                name=name,
                docstring=None,
                parameters=[
                    stub_types.Parameter(name="*args", type=None),
                    stub_types.Parameter(name="**kwargs", type=None)
                ],
                return_type="Any",
                static=static
            )
        )

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
            continue  # TODO: Temp, let's start by fixing the other functions first

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
