import inspect
import typing

from .. import stub_types, maya_info


BUILTIN_TYPES = (int, float, str, bool, tuple, list, dict)


def generate_property(name: str, prop_type: typing.Any) -> stub_types.Property:
    default = None
    if isinstance(prop_type, BUILTIN_TYPES) or prop_type is None:
        default = repr(prop_type)

    type_name = type(prop_type).__name__
    if prop_type is None:
        type_name = "None"

    return stub_types.Property(
        name=name,
        type=type_name,
        default=default
    )


def generate_method(member_name: str, member: typing.Any) -> stub_types.Method:
    static = isinstance(member, staticmethod)
    if static:
        method_docstring = inspect.getdoc(member.__func__)
    else:
        method_docstring = inspect.getdoc(member)

    return stub_types.Method(
        ref=member,
        name=member_name,
        return_type="Any",
        docstring=method_docstring,
        parameters=None,
        static=static
    )


def generate_class(class_ref: type) -> stub_types.Class:
    name = class_ref.__name__

    base_classes = [x for x in class_ref.__bases__ if x is not object]
    base_classes_names = [x.__name__ for x in base_classes]

    methods: list[stub_types.Method] = []
    properties: list[stub_types.Property] = []
    for member_name, member in class_ref.__dict__.items():
        if member_name in {"__class__", "__doc__", "__module__", "__weakref__", "__dict__", "__repr__", "__str__", "__new__"}:
            continue

        if (
            inspect.isfunction(member) or
            inspect.ismethod(member) or
            inspect.ismethoddescriptor(member) or
            inspect.isbuiltin(member)
        ):
            methods.append(generate_method(member_name, member))

        elif inspect.isgetsetdescriptor(member):
            properties.append(
                stub_types.PropertyGetSet(member_name,
                                          type="Any",
                                          docstring=member.__doc__,
                                          can_set=True)
            )

        # check if it's a static type
        elif isinstance(member, BUILTIN_TYPES) or member is None:
            properties.append(generate_property(member_name, member))

        else:
            properties.append(generate_property(member_name, member))

    return stub_types.Class(ref=class_ref,
                            name=name,
                            base_class_names=base_classes_names,
                            docstring=class_ref.__doc__,
                            methods=methods,
                            properties=properties)


def generate_classes(module: str) -> list[stub_types.Class]:
    class_references = maya_info.get_classes(module)
    if not class_references:
        return []

    classes: list[stub_types.Class] = []

    for class_ref in class_references:
        if class_ref is object:
            continue

        classes.append(generate_class(class_ref))

    return classes
