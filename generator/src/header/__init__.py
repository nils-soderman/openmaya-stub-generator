import os

__all__ = ["get", "get_default"]


def _get_header_path(name: str) -> str:
    current_dir = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(current_dir, name)


def _read_header(name: str) -> str | None:
    header_filepath = _get_header_path(name)
    if not os.path.isfile(header_filepath):
        return None

    with open(header_filepath, 'r', encoding='utf-8') as f:
        return f.read()


def _get_header(name: str, variables: dict[str, str] | None) -> str | None:
    if header := _read_header(name):
        if variables:
            for key, value in variables.items():
                header = header.replace(f"{{{key}}}", value)
        return header

    return None


def get_default(variables: dict[str, str] | None) -> str:
    if header := _get_header("header.pyi", variables):
        return header

    raise FileNotFoundError("Default header file 'header.pyi' not found.")


def get(namespace: str, variables: dict[str, str] | None) -> str:
    if header := _get_header(f"{namespace}_header.pyi", variables):
        return header

    return get_default(variables)
