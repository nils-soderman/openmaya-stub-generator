import importlib
import builtins
import inspect
import json
import re
import os


BUILTIN_NAMES = {x for x in dir(builtins) if isinstance(getattr(builtins, x), type)}
LITERAL_VALUES = {"True", "False", "0", "1", "-1", "2", "3"}

MAYA_OBJECT_PREFIX_REGEX = re.compile(r"^M[A-Z]")

TYPE_CONVERSION_FILEPATH = os.path.join(os.path.dirname(__file__), 'type_conversion.json')
with open(TYPE_CONVERSION_FILEPATH, 'r', encoding='utf-8') as f:
    TYPE_CONVERSION: dict[str, str] = json.load(f)


def convert_type(type_str: str) -> str:
    type_str_lowered = type_str.lower()

    if type_str_lowered in BUILTIN_NAMES:
        return type_str_lowered

    if type_str_lowered in TYPE_CONVERSION:
        return TYPE_CONVERSION[type_str_lowered]
    return type_str


def split_outside_nested(
    text: str,
    delimiter: str | list[str],
    open_chars: str = "([",
    close_chars: str = ")]",
    maxsplit: int = -1
) -> list[str]:
    """
    Split a string on one or more delimiters, ignoring delimiters inside nested pairs.

    Args:
        text: Input string.
        delimiter: Delimiter(s) to split on. Can be a string or a list of strings.
        open_chars: Opening characters for nesting.
        close_chars: Closing characters for nesting.
        maxsplit: Maximum number of splits to do. -1 means no limit.

    Example:
        split_outside_nested("a, func(b, c) or [x, y]", [",", " or "], "([", ")]")
        # Returns: ['a', 'func(b, c)', '[x, y]']
    """
    if isinstance(delimiter, str):
        delimiters = [delimiter]
    else:
        delimiters = sorted(delimiter, key=len, reverse=True)  # Longest first

    parts: list[str] = []
    buffer = ""
    depth = 0
    i = 0
    n = len(text)
    splits = 0
    while i < n:
        char = text[i]
        if char in open_chars:
            depth += 1
            buffer += char
            i += 1
            continue
        elif char in close_chars:
            depth = max(0, depth - 1)
            buffer += char
            i += 1
            continue

        if depth == 0 and (maxsplit < 0 or splits < maxsplit):
            matched = False
            for delim in delimiters:
                if text.startswith(delim, i):
                    if buffer.strip():
                        parts.append(buffer.strip())
                    buffer = ""
                    i += len(delim)
                    splits += 1
                    matched = True
                    break
            if matched:
                continue

        buffer += char
        i += 1

    if buffer.strip():
        parts.append(buffer.strip())
    return parts


def guess_python_from_desc_type(type_str: str) -> str:
    """
    Using regex patterns, guess the python type from the description type
    """
    if re.match(r'^int[A-Z]$', type_str):  # int[X]
        return "int"

    if re.match(r'^[Nn]um[A-Z]$', type_str):  # Num[X] or num[X]
        return "int"

    if re.match(r'^[a-z]Index$', type_str):  # [x]Index
        return "int"

    if re.match(r'^index[A-Z]$', type_str):  # index[xX]
        return "int"

    if re.match(r'^is[A-Z]\w*$', type_str):  # is[Word]
        return "bool"

    if re.match(r'^[A-z]*Name$', type_str):  # [A-z]Name
        return "str"

    return type_str


def get_python_type_from_desc(desc: str) -> str:
    """
    Get the Python type from a description (from the online documentation), 
    some examples of what the desc may be:
        - Float
        - (String, Double, Integer)
        - [MObject, ...]
        - List of Strings
    """
    # Sanitize input
    desc = re.sub(r'<[^>]+>', '', desc)  # Remove HTML tags that may be left if the online docs html is broken
    desc = re.sub(r'[*#]', '', desc).strip()  # Remove some illegal characters
    desc = re.sub(r'^the new ', "", desc, flags=re.IGNORECASE).strip()
    desc = re.sub(r'^a ', "", desc, flags=re.IGNORECASE).strip()
    desc = desc.removeprefix("unsigned ").strip()

    # Remove unmatched closing bracket
    if desc.count(')') > desc.count('('):
        desc = desc.replace(')', '', desc.count(')') - desc.count('('))

    if desc.endswith(".") and not desc.endswith("..."):
        desc = desc[:-1].strip()

    desc_lower = desc.lower()

    # Tuples: "tuple of strings" -> "tuple[str, ...]"
    # Lists: "list of floats" -> "list[float]"
    # Sequence: "Sequence of floats" -> "Sequence[float]"
    for prefix, py_type, is_tuple in [
        ("tuple of ", "tuple", True),
        ("tuples of ", "tuple", True),
        ("tuples containing ", "tuple", True),
        ("list of ", "list", False),
        ("sequence of ", "Sequence", False),
        ("seq of ", "Sequence", False),
    ]:
        if desc_lower.startswith(prefix):
            inner_content = desc[len(prefix):].strip()
            if re.match(r'^[\(\[]', inner_content):  # starts with ( or [
                inner_content = inner_content.strip(" ()[]")
                inner_types = split_outside_nested(inner_content, ",")
            else:
                inner_types = inner_content.split(" or ")
            inner_types = [t.strip().removesuffix("s").removesuffix("'") for t in inner_types]
            inner_types = [
                re.sub(r'^(?:[1-9]|two|three|four|five|six|seven|eight)\s+', '', x, flags=re.IGNORECASE) for x in inner_types
            ]
            inner_types = [get_python_type_from_desc(t) for t in inner_types]
            if is_tuple:
                return f"{py_type}[{'|'.join(inner_types)},...]"

            # Make sure there are no duplicates in list types
            inner_types = list(dict.fromkeys(inner_types))
            return f"{py_type}[{'|'.join(inner_types)}]"

    # Split by delimiters "X , Y or Z"
    if " or " in desc or "," in desc:
        split_types = split_outside_nested(desc, [",", " or "])
        if len(split_types) > 1:
            return "|".join(get_python_type_from_desc(t) for t in split_types)

    # Tuples: "(X, Y, Z)" -> "tuple[X, Y, Z]"
    if desc.startswith("(") and desc.endswith(")"):
        desc_inner = desc[1:-1].strip()
        inner_types = split_outside_nested(desc_inner, ",")
        inner_types = [get_python_type_from_desc(t) for t in inner_types]

        # ellipsis must be the 2nd element if present
        if inner_types[-1] == "..." and len(inner_types) > 2:
            return f"tuple[{inner_types[0]},...]"

        inner_type_str = ",".join(inner_types)
        return f"tuple[{inner_type_str}]"

    # Lists: "[X, Y, Z]" -> "list[X|Y|Z]"
    if desc.startswith("[") and desc.endswith("]"):
        desc_inner = desc[1:-1].strip()
        inner_types = split_outside_nested(desc_inner, ",")
        inner_types = [get_python_type_from_desc(t) for t in inner_types]
        inner_types = list(dict.fromkeys(inner_types))  # Make sure types are unique
        if "..." in inner_types:
            inner_types.remove("...")
        inner_type_str = "|".join(inner_types)
        return f"list[{inner_type_str}]"

    # types that end with " constant" are enums represented as int
    if desc_lower.endswith(" constant"):
        return "int"

    if desc_lower.endswith("reference to self"):
        return "Self"

    if "/" in desc:
        return "|".join(get_python_type_from_desc(x) for x in desc.split("/"))

    desc = convert_type(desc)
    desc = guess_python_from_desc_type(desc)
    desc = add_maya_module_prefix(desc)

    # If type contains a illigale character at this point, return Any
    if any(x in desc for x in (" ", ":")):
        print(f'Could not convert documented type "{desc}" to a Python type')
        desc = "Any"

    if desc in LITERAL_VALUES:
        desc = f"Literal[{desc}]"

    return desc


g_current_module_name: str | None = None


def add_maya_module_prefix(type_str: str) -> str:
    if MAYA_OBJECT_PREFIX_REGEX.search(type_str) is None:
        return type_str

    if g_current_module_name is None:
        raise RuntimeError("g_current_module_name is not set")

    if "." in type_str:
        cls_name = type_str.partition(".")[0]
    else:
        cls_name = type_str

    current_module = importlib.import_module(g_current_module_name)
    if hasattr(current_module, cls_name):
        return type_str

    if "api" in g_current_module_name.lower():
        other_modules = (("maya.api.OpenMaya", "om"),
                         ("maya.api.OpenMayaAnim", "oma"),
                         ("maya.api.OpenMayaRender", "omr"),
                         ("maya.api.OpenMayaUI", "omu"))
    else:
        other_modules = ()

    for module_name, module_alias in other_modules:
        if module_name == g_current_module_name:
            continue

        module = importlib.import_module(module_name)
        if hasattr(module, cls_name):
            return f"{module_alias}.{type_str}"

    print(f'Could not find maya type: "{type_str}", defaulting to Any')
    return "Any"
