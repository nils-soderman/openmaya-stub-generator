from . import stub_types


BUILTIN_MODULES = {
    "sys.": "import sys"
}

MAYA_MODULES = {
    "om.": "import maya.api.OpenMaya as om",
    "oma.": "import maya.api.OpenMayaAnim as oma",
    "omr.": "import maya.api.OpenMayaRender as omr",
    "omu.": "import maya.api.OpenMayaUI as omu",
}

TYPING_IMPORTS = {
    "Sequence",
    "Callable",
    "Literal",
    "Any",
    "Self"
}


class ImportCollector:
    def __init__(self) -> None:
        self.builtins: set[str] = set()
        self.imports: set[str] = set()
        self.typing_imports: set[str] = set()

    def __str__(self) -> str:
        return_value = "\n".join(sorted(self.imports))
        if self.typing_imports:
            return_value += f"\nfrom typing import {', '.join(sorted(self.typing_imports))}"

        if self.builtins:
            return_value += "\n" + "\n".join(sorted(self.builtins))

        return return_value

    def collect_from_classes(self, classes: list[stub_types.Class]) -> None:
        for cls in classes:
            for base in cls.base_class_names:
                self._collect_from_type_str(base)

            for prop in cls.properties:
                self._collect_from_type_str(prop.type)

            for method in cls.methods:
                self._collect_from_function(method)
                if method.overloads:
                    self.typing_imports.add("overload")
                    for overload in method.overloads:
                        self._collect_from_function(overload)

    def _collect_from_function(self, func: stub_types.Function) -> None:
        if func.parameters:
            for param in func.parameters:
                if param.type:
                    self._collect_from_type_str(param.type)
                    if param.default:
                        self._collect_from_type_str(param.default)

        if func.return_type:
            self._collect_from_type_str(func.return_type)

    def _collect_from_type_str(self, type_str: str) -> None:
        for prefix, import_stmt in BUILTIN_MODULES.items():
            if type_str.startswith(prefix):
                self.imports.add(import_stmt)

        for maya_prefix, import_stmt in MAYA_MODULES.items():
            if type_str.startswith(maya_prefix):
                self.imports.add(import_stmt)

        for typing_type in TYPING_IMPORTS:
            if typing_type in type_str:
                self.typing_imports.add(typing_type)
