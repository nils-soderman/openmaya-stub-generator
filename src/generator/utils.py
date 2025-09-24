from .. import resources
TYPE_CONVERSION = resources.load("type_conversion.jsonc")


def convert_type(type_str: str) -> str:
    if type_str in TYPE_CONVERSION:
        return TYPE_CONVERSION[type_str]
    return type_str
