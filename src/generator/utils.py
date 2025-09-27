import builtins
from .. import resources

TYPE_CONVERSION = resources.load("type_conversion.jsonc")

BUILTIN_NAMES = {x for x in dir(builtins) if isinstance(getattr(builtins, x), type)}

def convert_type(type_str: str) -> str:
    if type_str.lower() in BUILTIN_NAMES:
        return type_str.lower()

    if type_str in TYPE_CONVERSION:
        return TYPE_CONVERSION[type_str]
    return type_str
