from .documentation.patch_documentation import Patch_Documentation
from .manual_fix.patch_manualfix import Patch_ManualFix
from .patch_bultins import Patch_BuiltinMethods
from .patch_assume_arg_type import Patch_AssumeParameterType
from .patch_safe_arg_name import Patch_SafeParameterName
from .patch_static_self_return import Patch_StaticSelfReturn
from .patch_default_value_enum import Patch_DefaultValueEnum


ALL_PATCHES = sorted(
    [
        Patch_Documentation,
        Patch_ManualFix,
        Patch_BuiltinMethods,
        Patch_AssumeParameterType,
        Patch_SafeParameterName,
        Patch_StaticSelfReturn,
        Patch_DefaultValueEnum,
    ],
    key=lambda x: x.ORDER
)
