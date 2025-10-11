from .patch_static_self_return import Patch_StaticSelfReturn
from .patch_safe_arg_name import Patch_SafeParameterName
from .patch_assume_arg_type import Patch_AssumeParameterType


ALL_PATCHES = sorted(
    [
        Patch_StaticSelfReturn,
        Patch_SafeParameterName,
        Patch_AssumeParameterType
    ],
    key=lambda x: x.ORDER
)
