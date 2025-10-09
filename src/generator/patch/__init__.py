from .patch_static_self_return import PatchStaticSelfReturn

ALL_CLASS_PATCHES = sorted([
    PatchStaticSelfReturn
], key=lambda x: x.ORDER)
