import builtins
import json
import re
import os


BUILTIN_NAMES = {x for x in dir(builtins) if isinstance(getattr(builtins, x), type)}
LITERAL_VALUES = {"True", "False", "0", "1", "-1", "2", "3"}

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

    # If type contains a illigale character at this point, return Any
    if any(x in desc for x in (" ", ":")):
        print(f'Could not convert documented type "{desc}" to a Python type')
        desc = "Any"

    if desc in LITERAL_VALUES:
        desc = f"Literal[{desc}]"

    return desc


def extract_collection_type(desc: str, prefix: str, py_type: str) -> str | None:
    desc_lower = desc.lower()
    if desc_lower.startswith(prefix):
        inner_content = desc.removeprefix(prefix).strip()
        inner_content = inner_content.removesuffix("s").strip()
        inner_type = get_python_type_from_desc(inner_content)
        return f"{py_type}[{inner_type}{',...' if py_type == 'tuple' else ''}]"
    return None


def old(desc: str):
    desc = re.sub(r'<[^>]+>', '', desc)  # Remove HTML tags that may be left if the online docs html is broken
    desc = desc.replace('*', '')
    desc = desc.strip()

    bracket_list_pattern = r'(?<!list)\[(?!,)([^\[\]]+)\]'
    if re.search(bracket_list_pattern, desc):
        def __replace_bracket_list(match):
            inner_content = match.group(1)
            types = []
            for x in inner_content.split(','):
                if x.strip() == "...":
                    continue
                converted_type = get_python_type_from_desc(x)
                if converted_type not in types:
                    types.append(converted_type)

            return f"list[{'|'.join(types)}]"

        desc = re.sub(bracket_list_pattern, __replace_bracket_list, desc)

    if " or " in desc:
        types = re.split(r"\sor\s|,\s*", desc)
        return "|".join(get_python_type_from_desc(t) for t in types)

    if "/" in desc:
        types = desc.split("/")
        return_type = "|".join(get_python_type_from_desc(t) for t in types)
        if return_type == "True|False":
            return "bool"
        return return_type

    if desc.startswith("(") and desc.endswith(")"):
        # Only split on commas that are not inside parentheses
        # [, x]

        # types = desc[1:-1].split(",")
        types = split_outside_nested(desc[1:-1], ',', '(', ')')

        all_types: list[str] = []
        optionals_indices = []
        for x in types:
            t = x.removesuffix("[")
            if t.endswith("]") and "[" not in t:
                t = t[:-1]
                optionals_indices.append(len(all_types))

            t = get_python_type_from_desc(t)

            all_types.append(t)

        if all_types and all_types[-1] == "...":
            types = set(all_types)
            types.discard("...")

            all_types = list(types)
            types_str = "|".join(all_types) + ',...'
        elif optionals_indices:
            types_str = ",".join(all_types)
            other_version = ",".join(x for i, x in enumerate(all_types) if i not in optionals_indices)
            return f"tuple[{types_str}]|tuple[{other_version}]"
        else:
            types_str = ",".join(all_types)

        return f"tuple[{types_str}]"

    desc_processed = desc.strip()
    if desc_processed.endswith(".") and not desc_processed.endswith("..."):
        desc_processed = desc_processed[:-1].strip()

    if desc_processed.lower().startswith("the new "):
        desc_processed = desc_processed[len("the new "):].strip()

    if desc_processed.lower().endswith(" constant"):
        return "int"  # This is an "enum" type

    tuple_pattern = r'^(?:tuple of |tuples containing )(.+)$'
    if match := re.match(tuple_pattern, desc_processed.lower()):
        inner_type = match.group(1).strip()
        inner_type = inner_type.removesuffix("s")
        inner_type_name = get_python_type_from_desc(inner_type)
        if inner_type_name.startswith("tuple[") and inner_type_name.endswith("]"):
            return inner_type_name
        return f"tuple[{inner_type_name}, ...]"

    if desc_processed.lower().startswith("list of "):
        inner_type = desc_processed[len("list of "):].strip()
        inner_type = inner_type.removesuffix("s")
        inner_type_name = get_python_type_from_desc(inner_type)
        return f"list[{inner_type_name}]"

    if desc_processed.lower().startswith("sequence of ") or desc_processed.lower().startswith("seq of "):
        inner_type = desc_processed.partition(" of ")[2].strip()
        inner_type = inner_type.removesuffix("s").removesuffix("'").strip()
        inner_type_name = get_python_type_from_desc(inner_type)
        return f"Sequence[{inner_type_name}]"

    if desc_processed.lower().endswith("reference to self"):
        return "Self"

    type_name = convert_type(desc_processed)

    if any(x in type_name for x in {" ", "::"}):
        return "Any"

    if re.match(r'^([a-z]Index|index[A-Z])$', type_name):
        return "int"

    if re.match(r'^num[A-Z]$', type_name):
        return "int"

    if desc_processed.lower().endswith("name"):
        return "str"

    return type_name
