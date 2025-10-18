from .. import interface
from . import index, page


class OpenMaya2_Parser(interface.ParserBase):
    def get_namespaces(self, version: int) -> list[interface.Namespace]:
        return index.get_namespaces(version, self.use_cache)

    def get_namespace(self, namespace: str, version: int) -> interface.Namespace | None:
        return super().get_namespace(namespace.removeprefix("api."), version)

    def get_index(self, namespace: interface.Namespace) -> interface.Index:
        return index.get_namespace_index(namespace, self.use_cache)

    def parse_class_page(self, url: str) -> interface.Page:
        return page.parse(url, self.use_cache)
