import shutil
import os


def copy_stubs(target_dir: str):
    current_dir = os.path.dirname(__file__)
    stubs_path = os.path.join(current_dir, 'stubs')
    for file in os.listdir(stubs_path):
        if file.endswith('.pyi'):
            shutil.copy(os.path.join(stubs_path, file), target_dir)
