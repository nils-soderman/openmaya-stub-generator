"""

"""

from .base import PatchBase
from .documentation.parser import signature

# These docstrings are not really adding any info and just takes up space
BANNED_DOCSTRINGS = {
    "Initialize self.  See help(type(self)) for accurate signature.",

    "Return self>=value.",
    "Return self<=value.",
    "Return self>value.",
    "Return self<value.",
    "Return self==value.",
    "Return self!=value.",

    "Return self+value.",
    "Return value+self.",
    "Return value-self.",
    "Return self*value.",
    "Return value*self.",
    "Return value/self.",
    "Return self|value.",
    "Return value|self.",

    "Return len(self).",

    "Return self[key].",
    "Delete self[key].",
    "Set self[key] to value.",
    "Return key in self.",

    "Implement self+=value.",
    "Implement self-=value.",
    "Implement self*=value.",
}


class Patch_Docstring(PatchBase):
    ORDER = 1000

    def patch_method(self, class_, method, overload=None):
        if not method.docstring:
            return

        if method.docstring in BANNED_DOCSTRINGS:
            method.docstring = None
            return

        # Remove signatures from the docstring
        signatures = signature.extract_signatures_from_docstring(method.docstring, method.name)
        for sig in signatures:
            method.docstring = method.docstring.replace(sig, "").strip()
