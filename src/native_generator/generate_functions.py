from .. import stub_types, maya_info

def generate_functions(module: str) -> list[stub_types.Function]:
    function_references = maya_info.get_functions(module)
    if not function_references:
        return []

    functions: list[stub_types.Function] = []

    # Right now only OpenMaya has 3 functions that I have no idea what they do
    # No need to do anything fancy here yet
    for function_ref in function_references:
        functions.append(
            stub_types.Function(
                ref=function_ref,
                name=function_ref.__name__,
                return_type="Any",
                docstring=function_ref.__doc__
            )
        )

    return functions
