""" 
Static methods cannot return 'Self', make them return the class instead
"""

from .base import PatchBase


class Patch_StaticSelfReturn(PatchBase):
    def patch_class(self, class_):
        for method in class_.methods:
            if method.static and method.return_type == "Self":
                method.return_type = class_.name
