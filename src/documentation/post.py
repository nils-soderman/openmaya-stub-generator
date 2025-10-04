import typing
import re


class SignatureParameter(typing.NamedTuple):
    name: str
    default: str | None
    return_type: str | None = None
    param_type: str | None = None


def parse_signature(signature: str) -> tuple[list[SignatureParameter], str | None]:
    """
    parse a signature e.g. "function(arg1, arg2=5) -> return_type"
    """
    function_part, _, return_type = signature.partition("->")

    function_part = function_part.strip()
    return_type = return_type.strip() if return_type else None

    match = re.match(r'^[^(]+\((.*)\)$', function_part)
    if not match:
        return [], return_type

    param_str = match.group(1).strip().rstrip(")")
    if not param_str:
        return [], return_type

    params: list[SignatureParameter] = []
    for p in param_str.split(','):
        name, _, default = p.partition('=')
        name = name.strip()

        param_type = None
        if " " in name:
            param_type, _, name = name.partition(" ")
            param_type = param_type.strip()

        params.append(SignatureParameter(name=name.strip(), default=default.strip() or None, param_type=param_type))

    return params, return_type or return_type


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
    match = re.search(pattern, docstring)
    if match:
        return match.group(1).strip()