import typing
import json
import os
import re


def load_module_resource(module: str, file: str) -> dict[str, typing.Any]:
    module_path = module.replace('.', os.sep)
    return load_resource(os.path.join(module_path, file))


def load_resource(file: str) -> dict[str, typing.Any]:
    path = os.path.join(os.path.dirname(__file__), file)
    if os.path.exists(path):
        with open(path, 'r') as f:
            content = f.read()

            # Remove comments (//...) for JSONC
            # This is unsafe if the double slashes are inside values (e.g. key: "http://example.com")
            # Should be safe for this package's use cases, otherwise just switch to a proper JSONC parser
            content = re.sub(r'//.*', '', content)

            return json.loads(content)

    return {}
