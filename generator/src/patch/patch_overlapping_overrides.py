""" 
Patch overlapping overrides to combine them and return using | operator
"""
from .base import PatchBase


class Patch_OverlappingOverloads(PatchBase):
    ORDER = 1000

    def patch_method(self, class_, method, overload=None):
        if overload is not None:
            return

        unique_overloads = [method]
        for overload in list(method.overloads):
            matching_overload = next(
                (x for x in unique_overloads if x.parameters == overload.parameters),
                None
            )

            if matching_overload:
                method.overloads.remove(overload)
                if matching_overload.return_type != overload.return_type:
                    matching_overload.return_type = f"{matching_overload.return_type}|{overload.return_type}"

            else:
                unique_overloads.append(overload)
