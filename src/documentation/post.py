import typing
import re


class SignatureParameter(typing.NamedTuple):
    name: str
    default: str | None


def parse_signature_params(signature: str) -> list[SignatureParameter]:
    """
    parse a signature e.g. "function(arg1, arg2=5)"
    """
    params = []
    match = re.match(r'^[^(]+\((.*)\)$', signature)
    if not match:
        return params

    param_str = match.group(1)
    for p in param_str.split(','):
        name, _, default = p.partition('=')
        params.append(SignatureParameter(name=name.strip(), default=default.strip() or None))

    return params
