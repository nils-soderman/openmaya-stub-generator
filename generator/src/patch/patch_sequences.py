""" 
Patch sequence support
"""

from ..stub_types import Class, Method, Parameter, Property

from .base import PatchBase

SEQUENCE_TYPES = {
    "MVector": "float",
    "MPoint": "float",
    "MColor": "float",
    "MFloatVector": "float",
    "MFloatMatrix": "float",
    "MEulerRotation": "float",
    "MFloatPoint": "float",
    "MMatrix": "float",
    "MQuaternion": "float",
}

CONVERT_TABLE = {
    "MFloat": "float",
    "MDouble": "float",
    "MInt": "int",
    "MInt64": "int",
    "MUint": "int",
    "MUint64": "int",
    "MUInt64": "int",
    "MCallbackId": "int",
    "MString": "str",
}


class Patch_Sequences(PatchBase):
    def patch_class(self, class_: Class):
        if class_.name.endswith("Array"):
            seq_type = class_.name.removesuffix("Array")

        elif class_.name.endswith("ArrayData"):
            seq_type = class_.name.removesuffix("ArrayData")
            if seq_type.startswith("MFn"):
                seq_type = "M" + seq_type.removeprefix("MFn")

        elif class_.name in SEQUENCE_TYPES:
            seq_type = SEQUENCE_TYPES[class_.name]

        else:
            return

        seq_type = CONVERT_TABLE.get(seq_type, seq_type)

        class_.base_class_names.append(f"collections.abc.Sequence[{seq_type}]")

        for method in class_.methods:
            if method.name == "__getitem__":
                method.return_type = seq_type

            elif method.name == "__setitem__":
                if method.parameters and len(method.parameters) >= 2:
                    method.parameters[1].type = seq_type

            elif method.name == "append":
                if method.parameters and len(method.parameters) == 1 and method.parameters[0].name == "item":
                    method.parameters[0].type = seq_type

            elif method.name == "insert":
                if method.parameters and len(method.parameters) == 2 and method.parameters[1].name == "item":
                    method.parameters[1].type = seq_type

            elif method.name == "remove":
                if method.parameters and len(method.parameters) == 1 and method.parameters[0].name == "item":
                    method.parameters[0].type = seq_type

            elif method.name == "setLength":
                if not method.parameters:
                    method.parameters = [
                        Parameter(name="length", type="int")
                    ]
                    method.return_type = "Self"
