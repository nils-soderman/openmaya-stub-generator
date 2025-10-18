import types
import sys
import os


def pytest_sessionstart(session):
    env_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'env'))
    sys.path.append(env_path)

    sys.modules['maya'] = types.ModuleType('maya')
    sys.modules['maya.api'] = types.ModuleType('maya.api')
    sys.modules['maya.api.OpenMaya'] = types.ModuleType('maya.api.OpenMaya')

