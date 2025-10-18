import builtins
import json
import re
import os


BUILTIN_NAMES = {x for x in dir(builtins) if isinstance(getattr(builtins, x), type)}

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
    close_chars: str = ")]"
) -> list[str]:
    """
    Split a string on one or more delimiters, ignoring delimiters inside nested pairs.

    Args:
        text: Input string.
        delimiter: Delimiter(s) to split on. Can be a string or a list of strings.
        open_chars: Opening characters for nesting.
        close_chars: Closing characters for nesting.

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

        if depth == 0:
            matched = False
            for delim in delimiters:
                if text.startswith(delim, i):
                    if buffer.strip():
                        parts.append(buffer.strip())
                    buffer = ""
                    i += len(delim)
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
    if re.match(r'^int[A-Z]$', type_str):  # intR, intG, intB
        return "int"

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
    desc = re.sub(r'<[^>]+>', '', desc)  # Remove HTML tags that may be left if the online docs html is broken
    desc = desc.replace('*', '')
    desc = desc.strip()

    desc_lower = desc.lower()

    # Split by delimiters "X , Y or Z"
    if " or " in desc or "," in desc:
        split_types = split_outside_nested(desc, [",", " or "])
        if len(split_types) > 1:
            return "|".join(get_python_type_from_desc(t) for t in split_types)

    # Tuples: "tuple of strings" -> "tuple[str, ...]"
    if desc_lower.startswith("tuple of "):
        inner_content = desc.removeprefix("tuple of ").strip()
        inner_content = inner_content.removesuffix("s").strip()
        inner_type = get_python_type_from_desc(inner_content)
        return f"tuple[{inner_type}, ...]"

    # Tuples: "(X, Y, Z)" -> "tuple[X, Y, Z]"
    if desc_lower.startswith("(") and desc_lower.endswith(")"):
        desc_inner = desc[1:-1].strip()
        inner_types = split_outside_nested(desc_inner, ",")
        inner_types = [get_python_type_from_desc(t) for t in inner_types]
        inner_type_str = ",".join(inner_types)
        return f"tuple[{inner_type_str}]"

    # types that end with " constant" are enums represented as int
    if desc_lower.endswith(" constant"):
        return "int"

    desc = convert_type(desc)
    desc = guess_python_from_desc_type(desc)

    return desc


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
