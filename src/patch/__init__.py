from .documentation.patch_documentation import Patch_Documentation
from .manual_fix.patch_manualfix import Patch_ManualFix
from .patch_bultins import Patch_BuiltinMethods
from .patch_assume_arg_type import Patch_AssumeParameterType
from .patch_safe_arg_name import Patch_SafeParameterName
from .patch_static_self_return import Patch_StaticSelfReturn
from .patch_default_value_enum import Patch_DefaultValueEnum
from .patch_maya_types import Patch_MayaTypes
from .patch_sequences import Patch_Sequences
from .patch_overlapping_overrides import Patch_OverlappingOverloads


ALL_PATCHES = sorted(
    [
        Patch_Documentation,
        Patch_ManualFix,
        Patch_BuiltinMethods,
        Patch_AssumeParameterType,
        Patch_SafeParameterName,
        Patch_StaticSelfReturn,
        Patch_DefaultValueEnum,
        Patch_MayaTypes,
        Patch_Sequences,
        Patch_OverlappingOverloads
    ],
    key=lambda x: x.ORDER
)
