from . import stub_types, utils
from .. import maya_info, documentation, resources

def generate_variables(module: str, doc_index: documentation.index.Index | None) -> list[stub_types.Variable]:
    variable_names = maya_info.get_variable_names(module)
    if not variable_names:
        return []

    variables: list[stub_types.Variable] = []

    for var_name in variable_names:
        var_type = "Any"
        var_default = None
        doc_var = None
        if doc_index:
            if doc_var := doc_index.get_variable_by_name(var_name):
                var_type = utils.convert_type(doc_var.type)
                if var_type == "dict":
                    var_type = "dict[str, Any]"
                else:
                    var_default = doc_var.default

            # For now, skip undocumented variables
            else:
                continue
        else:
            continue

        variables.append(stub_types.Variable(name=var_name, type=var_type, default=var_default))

    return variables