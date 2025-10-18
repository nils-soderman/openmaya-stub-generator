import builtins
from .. import resources

TYPE_CONVERSION = resources.load_resource("type_conversion.jsonc")

BUILTIN_NAMES = {x for x in dir(builtins) if isinstance(getattr(builtins, x), type)}

def convert_type(type_str: str) -> str:
    type_str_lowered = type_str.lower()

    if type_str_lowered in BUILTIN_NAMES:
        return type_str_lowered

    if type_str_lowered in TYPE_CONVERSION:
        return TYPE_CONVERSION[type_str_lowered]
    return type_str
