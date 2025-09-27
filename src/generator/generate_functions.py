from . import stub_types
from .. import maya_info, documentation, resources


def generate_functions(module: str, doc_index: documentation.index.Index | None) -> list[stub_types.Function]:
    function_references = maya_info.get_functions(module)
    if not function_references:
        return []

    functions: list[stub_types.Function] = []

    # Right now only OpenMaya has 3 functions that I have no idea what they do
    # No need to do anything fancy here yet
    for function_ref in function_references:
        docstring = function_ref.__doc__ or ""
        functions.append(stub_types.Function(name=function_ref.__name__, return_type="Any", docstring=docstring))

    return functions
