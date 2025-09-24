from . import stub_types
from .. import maya_info, documentation, resources


def generate_functions(module: str, doc_index: documentation.index.Index | None) -> list[stub_types.Function]:
    function_names = maya_info.get_functions(module)
    if not function_names:
        return []

    functions: list[stub_types.Function] = []

    # Right now only OpenMaya has 3 functions that I have no idea what they do
    # No need to do anything fancy here yet
    for func_name in function_names:
        functions.append(stub_types.Function(name=func_name, return_type="Any"))

    return functions
