""" 
Static methods cannot return 'Self', make them return the class instead
"""

from src.stub_types import Class, Method
from .base import PatchBase


class Patch_StaticSelfReturn(PatchBase):
    def patch_method(self, class_: Class, method: Method, overload: Method | None = None):
        if method.static and method.return_type == "Self":
            method.return_type = class_.name
