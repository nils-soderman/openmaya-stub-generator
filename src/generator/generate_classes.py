
from . import stub_types
from .. import maya_info, documentation, resources


def generate_class(class_name: str, doc: documentation.page.Page | None) -> stub_types.Class:
    docstring = ""

    if doc:
        if doc.detailed_description:
            docstring = doc.detailed_description.description

    return stub_types.Class(name=class_name, base_classes=[], docstring=docstring, methods=[], properties=[])


def generate_classes(module: str, doc_index: documentation.index.Index | None, use_cache: bool) -> list[stub_types.Class]:
    class_names = maya_info.get_classes(module)
    if not class_names:
        return []

    classes: list[stub_types.Class] = []

    for class_name in class_names:
        doc_page = None
        if doc_index:
            if doc_class := doc_index.get_class_by_name(class_name):
                doc_page = documentation.parse(doc_class.url, use_cache)

        classes.append(generate_class(class_name, doc_page))

    return classes
