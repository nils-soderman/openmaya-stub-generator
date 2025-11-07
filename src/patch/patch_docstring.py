"""

"""

from .base import PatchBase
from .documentation.parser import signature


class Patch_Docstring(PatchBase):
    ORDER = 1000

    def patch_method(self, class_, method, overload=None):
        if not method.docstring:
            return

        # Remove signatures from the docstring
        signatures = signature.extract_signatures_from_docstring(method.docstring, method.name)
        for sig in signatures:
            method.docstring = method.docstring.replace(sig, "").strip()
