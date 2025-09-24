import enum
import os

from . import generate_classes, generate_functions, generate_variables

from .. import maya_info, documentation


class Flags(enum.Flag):
    NONE = 0
    CACHE = enum.auto()


def generate_string(module: str, flags: Flags) -> str:
    version = maya_info.get_version()
    use_cache = bool(flags & Flags.CACHE)

    doc_namespace = next((x for x in documentation.get_namespaces(version, use_cache=use_cache) if x.name == module), None)
    doc_index = None
    if doc_namespace:
        doc_index = documentation.get_namespace_index(doc_namespace, use_cache=use_cache)

    header_filepath = os.path.join(os.path.dirname(os.path.dirname(__file__)), "template_header.pyi")
    with open(header_filepath, 'r', encoding='utf-8') as f:
        header = f.read()
    header = header.replace("{VERSION}", version)
    header = header.replace("{MODULE}", module)

    out_str = header
    if variables := generate_variables.generate_variables(module, doc_index):
        out_str += "\n\n"
        out_str += "\n".join(str(var) for var in variables)
    if classes := generate_classes.generate_classes(module, doc_index, use_cache=use_cache):
        out_str += "\n\n"
        out_str += "\n".join(str(cls) for cls in classes)
    if functions := generate_functions.generate_functions(module, doc_index):
        out_str += "\n\n"
        out_str += "\n".join(str(func) for func in functions)
    out_str += "\n"

    return out_str


def generate_file(module: str, out_path: str, flags: Flags = Flags.NONE) -> None:
    code = generate_string(module, flags=flags)

    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    with open(out_path, 'w', encoding='utf-8') as f:
        f.write(code)


def generate_stubs(out_dir: str, flags: Flags = Flags.NONE) -> None:
    for module in maya_info.get_api_modules():
        out_filepath = os.path.join(out_dir, f"{module}.pyi")
        generate_file(module, out_filepath, flags=flags)
