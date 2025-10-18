import time

from ..flags import Flags
from .. import stub_types


class PatchBase:
    ORDER = 100

    def __init__(self, module_name: str, version: int, flags: Flags) -> None:
        self.module_name = module_name
        self.flags = flags

    def apply_patch(self, variables: list[stub_types.Variable], classes: list[stub_types.Class], functions: list[stub_types.Function]):
        print(f"Applying patch {self.__class__.__name__} [{self.ORDER}]:")

        start_time = time.perf_counter()

        for variable in variables:
            self.patch_variable(variable)

        for class_ in classes:
            self.patch_class(class_)

        for function in functions:
            self.patch_function(function)

        end_time = time.perf_counter()

        print(f"\tPatch took {end_time - start_time:.2f} seconds")

    def patch_variable(self, variable: stub_types.Variable):
        pass

    def patch_class(self, class_: stub_types.Class):
        for method in class_.methods:
            self.patch_method(class_, method)
        for property in class_.properties:
            self.patch_property(property)

    def patch_method(self, class_: stub_types.Class, method: stub_types.Method):
        pass

    def patch_property(self, property: stub_types.Property):
        pass

    def patch_function(self, function: stub_types.Function):
        pass
