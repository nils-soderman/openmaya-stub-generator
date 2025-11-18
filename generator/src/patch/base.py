import time

from ..flags import Flags
from .. import stub_types


class PatchBase:
    ORDER = 100

    def __init__(self, module_name: str, version: int, flags: Flags) -> None:
        self.module_name = module_name
        self.flags = flags

    def is_valid(self) -> bool:
        return True

    def apply_patch(self, variables: list[stub_types.Variable], classes: list[stub_types.Class], functions: list[stub_types.Function]):
        if not self.is_valid():
            print(f"Skipping patch {self.__class__.__name__} [{self.ORDER}] as it is not valid for module '{self.module_name}'")
            return

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
            for overload in list(method.overloads):
                self.patch_method(class_, overload, method)

        for property in class_.properties:
            self.patch_property(class_, property)

    def patch_method(self, class_: stub_types.Class, method: stub_types.Method, overload: stub_types.Method | None = None):
        """ 
        Patch a method or an overload

        Parameters
            - class_: The class the method belongs to 
            - method: The method to patch
            - overload: If this is an overload, overload is the original method
        """
        pass

    def patch_property(self, class_: stub_types.Class, property: stub_types.Property):
        pass

    def patch_function(self, function: stub_types.Function):
        pass
