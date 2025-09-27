import inspect
import typing

import pkgutil
import maya.api.OpenMaya as om
import maya.api

import importlib


def get_version():
    return om.MGlobal.mayaVersion()


def get_api_modules() -> list[str]:
    return [name for _, name, _ in pkgutil.iter_modules(maya.api.__path__) if not name.startswith('_')]


def get_functions(module_name: str) -> list[typing.Callable]:
    module = getattr(maya.api, module_name)
    return [obj for name, obj in inspect.getmembers(module) if inspect.isbuiltin(obj)]


def get_classes(module_name: str) -> list[type]:
    module = importlib.import_module(f"maya.api.{module_name}")
    return [obj for name, obj in inspect.getmembers(module) if inspect.isclass(obj)]


def get_variable_names(module_name: str) -> list[str]:
    module = importlib.import_module(f"maya.api.{module_name}")
    return [name for name, obj in inspect.getmembers(module) if not (inspect.isfunction(obj) or inspect.ismethod(obj) or inspect.isbuiltin(obj) or inspect.isclass(obj)) and not name.startswith('__')]
