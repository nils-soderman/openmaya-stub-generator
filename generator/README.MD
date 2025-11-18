# OpenMaya Stub Generator

Generate python stub files for Autodesk OpenMaya modules.

## Generator Usage

1. Install the generator
2. Call the generator using the mayapy Python interpreter

```cmd
pip install git+https://github.com/nils-soderman/openmaya-stub-generator#subdirectory=generator --target="{INSTALL_LOCATION}"

cd "{INSTALL_LOCATION}"

"C:/Program Files/Autodesk/Maya{VERSION}/bin/mayapy.exe" -m openmaya_stub_generator "{OUTPUT_DIR}"
```

* Replace `{INSTALL_LOCATION}` with your desired installation path
* Replace `{VERSION}` with your Maya version
* Replace `{OUTPUT_DIR}` with the directory where you want the stub files to be generated

### CLI Options
Optional flags that can be included when running the command to generate the stub files:
| Option | Description |
|-|-|
| `--cache` | Cache the online documentation on disk, mainly for development when you re-run the generator multiple times |


## Issues

If you run into any issues with the generator, Please open a issue on the [GitHub repository](https://github.com/nils-soderman/openmaya-stub-generator/issues).

Contributions are always welcomed!
