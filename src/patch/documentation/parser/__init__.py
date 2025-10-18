from . import interface
from .OpenMaya2 import OpenMaya2_Parser


def get_parser(api2: bool, use_cache: bool = True) -> interface.ParserBase:
    if api2:
        return OpenMaya2_Parser(use_cache=use_cache)

    raise NotImplementedError("Only OpenMaya2 is supported at the moment.")
