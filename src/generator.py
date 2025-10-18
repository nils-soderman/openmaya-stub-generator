import os

from .native_generator import generate_classes, generate_functions, generate_variables

from . import maya_info

from .patch import ALL_PATCHES

from .flags import Flags
from . import header

MODULES = [
    "api.OpenMaya",
    "api.OpenMayaAnim",
    "api.OpenMayaFX",
    "api.OpenMayaUI"
]

def generate_string(module: str, flags: Flags) -> str:
    version = maya_info.get_version()

    header_str = header.get(module, {"VERSION": str(version), "MODULE": module})

    variables = generate_variables.generate_variables(module)
    classes = generate_classes.generate_classes(module)
    functions = generate_functions.generate_functions(module)

    for patch in ALL_PATCHES:
        patch(module, version, flags).apply_patch(variables, classes, functions)

    out_str = header_str

    # OpenMaya currently does not have any module-level variables that are meant to be accessed
    # if variables:
    #     out_str += "\n\n"
    #     out_str += "\n".join(str(var) for var in variables)

    if classes:
        out_str += "\n\n"
        out_str += "\n".join(str(cls) for cls in classes)

    if functions:
        out_str += "\n\n"
        out_str += "\n".join(str(func) for func in functions)

    return out_str + "\n"


def generate_file(module: str, out_path: str, flags: Flags = Flags.NONE) -> None:
    code = generate_string(module, flags=flags)

    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    with open(out_path, 'w', encoding='utf-8') as f:
        f.write(code)


def generate_stubs(out_dir: str, flags: Flags = Flags.NONE) -> None:
    for module in MODULES:
        relative_path = module.replace('.', os.sep) + '.pyi'
        out_filepath_abs = os.path.join(out_dir, relative_path)
        generate_file(module, out_filepath_abs, flags=flags)

        if module == "api.OpenMaya":  # TEMP DEV
            break
