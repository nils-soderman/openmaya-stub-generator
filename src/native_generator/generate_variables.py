from .. import stub_types
from .. import maya_info

def generate_variables(module: str) -> list[stub_types.Variable]:
    variable_names = maya_info.get_variable_names(module)
    if not variable_names:
        return []

    variables: list[stub_types.Variable] = []

    for var_name in variable_names:
        var_type = "Any"
        var_default = None

        variables.append(stub_types.Variable(name=var_name, type=var_type, default=var_default))

    return variables