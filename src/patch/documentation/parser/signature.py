""" 
Parse the function signatures from the docstring
"""

import typing
import re

from .. import convert_type

OBSOLETE_TAG = "[obsolete]"


class SignatureParameter(typing.NamedTuple):
    name: str
    param_type: str | None = None
    default: str | None = None


class ParsedSignature(typing.NamedTuple):
    parameters: list[SignatureParameter]
    return_type: str | None
    is_obsolete: bool = False


def extract_signatures_from_docstring(docstring: str, function_name: str, stop_search_at_text: bool = True) -> list[str]:
    """
    Retrieve all signatures of a function from a docstring.

    Args:
        docstring (str): The docstring containing the function signatures.
        function_name (str): The name of the function to search for.
        stop_search_at_text (bool): If True, only consider signatures at the top of the docstring.

    Returns:
        list[tuple[list[SignatureParameter], str | None]]: A list of tuples, each containing a list of
        SignatureParameter objects and an optional return type.
    """
    # Handle e.g. (Deprecated) at the start of the docstring
    if docstring.lstrip().startswith("("):
        docstring = re.sub(r'^\s*\([^)]+\)\s*', '', docstring)

    # Keep only the initial contiguous block of signatures (supports multi-line signatures)
    start_sig_re = re.compile(rf'^\s*{re.escape(function_name)}\s*\(')

    lines = docstring.splitlines()
    kept_lines: list[str] = []
    started = False
    paren_open = 0  # track '(' vs ')' while inside a signature

    for line in lines:
        if not started:
            if start_sig_re.match(line):
                started = True
                kept_lines.append(line)
                paren_open = line.count('(') - line.count(')')
            else:
                # ignore any preamble before first signature
                continue
        else:
            if paren_open > 0:
                kept_lines.append(line)
                paren_open += line.count('(') - line.count(')')
            else:
                if not line.strip():
                    # allow blank lines within the signatures block
                    kept_lines.append(line)
                    continue
                if start_sig_re.match(line):
                    kept_lines.append(line)
                    paren_open = line.count('(') - line.count(')')
                elif line.strip().startswith("->"):
                    # allow return type on a new line
                    kept_lines.append(line)
                elif stop_search_at_text:
                    # first normal text line after signatures -> stop
                    break

    truncated = "".join(kept_lines)

    return [function_name + "(" + x for x in convert_type.split_outside_nested(truncated, function_name + "(")]


def parse_signature(signature: str) -> ParsedSignature:
    """
    parse a signature e.g. "function(arg1, arg2=5) -> return_type"
    """
    obsolete = signature.lower().endswith(OBSOLETE_TAG)
    if obsolete:
        signature = signature[:-len(OBSOLETE_TAG)].rstrip()

    function_part, _, return_type = signature.partition("->")
    function_part = function_part.strip()
    
    return_type = return_type.strip()
    if not return_type:
        return_type = None

    match = re.match(r'^[^(]+\((.*)\)$', function_part)
    if not match:
        return ParsedSignature([], return_type, obsolete)

    param_str = match.group(1).strip()
    if not param_str:
        return ParsedSignature([], return_type, obsolete)
    
    # Replace [arg=] with arg=
    param_str = re.sub(r'\[\s*([^\]=]+)=\s*', r'\1=', param_str)

    # Replace [, with , to make sure we split on it. for optional params e.g. func(arg1[, arg2])
    param_str = re.sub(r'\[\s*,\s*', ',', param_str)

    # Split on commas that are not within brackets
    parm_split = convert_type.split_outside_nested(param_str, ",")

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

        params.append(SignatureParameter(name=name.strip(), param_type=param_type, default=default.strip() or None))

    return ParsedSignature(params, return_type or None, obsolete)

def extract_param_type_from_docstring(param_name: str, docstring: str) -> str | None:
    # Look for: "* param_name (Type) "
    pattern = rf'^\s*[\*\s]\s*{re.escape(param_name)}\s*\(([^)]+)\)'
    if match := re.search(pattern, docstring, re.MULTILINE):
        return match.group(1).strip()
