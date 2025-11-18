import shutil
import os


def copy_stubs(target_dir: str):
    current_dir = os.path.dirname(__file__)
    manually_typed_stubs_dir = os.path.join(current_dir, 'stubs')
    shutil.copytree(manually_typed_stubs_dir, target_dir, dirs_exist_ok=True)
