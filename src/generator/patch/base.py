from ...generator import stub_types


class PatchBaseClass:
    ORDER = 100

    @classmethod
    def apply(cls, classes: list[stub_types.Class]):
        for class_ in classes:
            cls().patch_class(class_)

    def patch_class(self, class_: stub_types.Class):
        pass
