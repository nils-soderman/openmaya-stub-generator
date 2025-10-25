import inspect
import typing

import maya.api.OpenMaya as om

import importlib


def get_version() -> int:
    return int(om.MGlobal.mayaVersion())


def get_functions(module_name: str) -> list[typing.Callable]:
    module = importlib.import_module(module_name)
    return [obj for name, obj in inspect.getmembers(module) if inspect.isbuiltin(obj)]


def get_classes(module_name: str) -> list[type]:
    module = importlib.import_module(module_name)
    return [obj for name, obj in inspect.getmembers(module) if inspect.isclass(obj)]


def get_variable_names(module_name: str) -> list[str]:
    module = importlib.import_module(module_name)
    return [name for name, obj in inspect.getmembers(module) if not (inspect.isfunction(obj) or inspect.ismethod(obj) or inspect.isbuiltin(obj) or inspect.isclass(obj)) and not name.startswith('__')]
