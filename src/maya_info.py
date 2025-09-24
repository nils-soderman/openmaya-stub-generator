import inspect

import pkgutil
import maya.api.OpenMaya as om
import maya.api

import importlib


def get_version():
    return om.MGlobal.mayaVersion()


def get_api_modules() -> list[str]:
    return [name for _, name, _ in pkgutil.iter_modules(maya.api.__path__) if not name.startswith('_')]


def get_functions(module_name: str) -> list[str]:
    module = getattr(maya.api, module_name)
    return [name for name, obj in inspect.getmembers(module) if inspect.isbuiltin(obj)]


def get_classes(module_name: str) -> list[str]:
    module = importlib.import_module(f"maya.api.{module_name}")
    return [x for x, y in inspect.getmembers(module) if inspect.isclass(y)]


def get_variables(module_name: str) -> list[str]:
    module = importlib.import_module(f"maya.api.{module_name}")
    return [x for x, y in inspect.getmembers(module) if not (inspect.isfunction(y) or inspect.ismethod(y) or inspect.isbuiltin(y) or inspect.isclass(y)) and not x.startswith('__')]
