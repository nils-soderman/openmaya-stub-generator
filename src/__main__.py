import argparse
import time
import os

from . import generator
from .flags import Flags

try:
    import maya.standalone
except ImportError:
    raise ImportError("This script must be run in the mayapy.exe interpreter.")

class MayaStandalone:
    def __enter__(self):
        print("Initializing Maya standalone...")
        try:
            maya.standalone.initialize()
        except RuntimeError:
            pass
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        try:
            maya.standalone.uninitialize()
        except RuntimeError:
            pass


def main() -> None:
    parser = argparse.ArgumentParser(description="Generate stubs for the OpenMaya 2.0 modules. This module must run in the mayapy interpreter.")

    parser.add_argument("output", type=str, help="Output file path for the generated stubs.")
    parser.add_argument(
        "--cache",
        action="store_true",
        help="Cache the online documentation to disk"
    )

    args = parser.parse_args()

    output_path = os.path.abspath(args.output)

    start_time = time.perf_counter()

    flags = Flags.NONE
    if args.cache:
        flags |= Flags.CACHE

    with MayaStandalone():
        generator.generate_stubs(output_path, flags=flags)

    elapsed_time = time.perf_counter() - start_time
    print(f"Stubs generated successfully in {elapsed_time:.2f} seconds.")


if __name__ == "__main__":
    main()
