import typing
import re

OBSOLETE_TAG = "[obsolete]"

class SignatureParameter(typing.NamedTuple):
    name: str
    default: str | None
    return_type: str | None = None
    param_type: str | None = None

class ParsedSignature(typing.NamedTuple):
    parameters: list[SignatureParameter]
    return_type: str | None
    is_obsolete: bool


def parse_signature(signature: str) -> ParsedSignature:
    """
    parse a signature e.g. "function(arg1, arg2=5) -> return_type"
    """
    obsolete = signature.lower().endswith(OBSOLETE_TAG)
    if obsolete:
        signature = signature[:-len(OBSOLETE_TAG)].rstrip()

    function_part, _, return_type = signature.partition("->")

    function_part = function_part.strip()
    return_type = return_type.strip() if return_type else None

    match = re.match(r'^[^(]+\((.*)\)$', function_part)
    if not match:
        return ParsedSignature([], return_type, obsolete)

    param_str = match.group(1).strip().rstrip(")")
    if not param_str:
        return ParsedSignature([], return_type, obsolete)
    
    # Replace [, with , to make sure we split on it. for optional params e.g. func(arg1[, arg2])
    param_str = re.sub(r'\[\s*,\s*', ',', param_str)

    # Split on commas that are not within brackets
    parm_split = split_on_commas_outside_parentheses(param_str, '[', ']')

    params: list[SignatureParameter] = []
    for p in parm_split:
        name, _, default = p.partition('=')
        name = name.strip()
        param_type = None

        if name.lower().startswith("sequence of "):
            param_type = name
            name = "arg"

        if name.startswith("[") and name.endswith("]"):
            param_type = name
            name = "arg"

        # signature sometimes are formatted like:
        # (arg1[, arg2])
        elif name.endswith("]") and not re.search(r'\[\d*\]$', name):
            name = name[:-1].strip()
            if not default:  # does this mean the arg is optional?
                default = "..."

        if " " in name:
            if name.count(" ") == 1:
                param_type, _, name = name.partition(" ")
                param_type = param_type.strip()
            elif " or " in name.lower():
                name = re.split(r'\s+or\s+', name, flags=re.IGNORECASE)[0]
                param_type = "Any"
            else:
                param_type = name
                name = "arg"

        if default.startswith("]"):
            default = default[1:].strip()

        params.append(SignatureParameter(name=name.strip(), default=default.strip() or None, param_type=param_type))

    return ParsedSignature(params, return_type or None, obsolete)


def extract_signature_from_docstring(docstring: str, function_name: str) -> list[str]:
    """
    Parse all signatures of a function from a docstring.

    Args:
        docstring (str): The docstring containing the function signatures.
        function_name (str): The name of the function to search for.

    Returns:
        list[tuple[list[SignatureParameter], str | None]]: A list of tuples, each containing a list of
        SignatureParameter objects and an optional return type.
    """
    pattern = rf'{function_name}\s*\(\s*([^)]*?)\s*\)(?:\s*->\s*(.*?))?(?=\s*{function_name}|\n|$)'

    matches = re.findall(pattern, docstring, re.MULTILINE | re.DOTALL)

    signatures: list[str] = []
    for match in matches:
        params_str, return_type = match
        params_str = re.sub(r'\s+', ' ', params_str.strip())

        return_type = return_type.strip() if return_type else "None"

        signatures.append(f"{function_name}({params_str}) -> {return_type}")

    return signatures

def extract_parameter_types_from_docstring(parameter_name: str, docstring: str) -> str | None:
    # Search for e.g. "* param_name (type) - desc."
    pattern = rf'\*\s*{re.escape(parameter_name)}\s*\(([^)]+)\)'
    match = re.search(pattern, docstring, re.IGNORECASE)
    if match:
        return match.group(1).strip()


def split_on_commas_outside_parentheses(text: str, parentheses_open: str, parentheses_close: str) -> list[str]:
    """Split text on commas that are not inside parentheses."""
    parm_split = []
    current_param = ""
    bracket_count = 0
    
    for char in text + ",":  # Add comma to flush last param
        if char == parentheses_open:
            bracket_count += 1
        elif char == parentheses_close:
            bracket_count = max(0, bracket_count - 1)
        elif char == "," and bracket_count == 0:
            if current_param.strip():
                parm_split.append(current_param.strip())
            current_param = ""
            continue
        
        current_param += char
    
    return parm_split