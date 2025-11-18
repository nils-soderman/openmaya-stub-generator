import typing

from dataclasses import dataclass, field


def indent(code: str, num: int) -> str:
    indent_str = '\t' * num
    return indent_str + "\n".join(
        f"{indent_str}{line.rstrip()}" if line.strip() else ""
        for line in code.splitlines()
    ).lstrip()


def safe_docstring(docstring: str):
    if docstring.endswith('"'):
        docstring = docstring[:-1] + '\\"'

    return docstring.replace('"""', '\\"\\"\\"')


@dataclass
class Variable:
    name: str
    type: str | None = None
    default: str | None = None

    def __str__(self) -> str:
        param_str = self.name
        if self.type:
            param_str += f":{self.type}"
        param_str += f"={self.default or '...'}"
        return param_str


@dataclass
class Parameter:
    name: str
    type: str | None = None
    default: str | None = None

    def __str__(self) -> str:
        param_str = self.name
        if self.type:
            param_str += f":{self.type}"
            if self.default == "None" and "None" not in self.type:
                param_str += "|None"
        if self.default:
            param_str += f"={self.default}"
        return param_str


@dataclass
class Function:
    ref: typing.Callable
    name: str
    return_type: str | None = None
    parameters: list[Parameter] | None = None
    docstring: str | None = None
    deprecated: bool = False
    overloads: list[typing.Self] = field(default_factory=list)

    def get_params_str(self) -> str:
        if self.parameters is None:
            return "*args"

        return ",".join(str(param) for param in self.parameters)

    def __str__(self) -> str:
        func_str = ""

        params_str = self.get_params_str()
        return_type = self.return_type or "Any"

        func_str += f"def {self.name}({params_str})->{return_type}:"

        if self.docstring:
            func_str += "\n" + indent(f'"""{safe_docstring(self.docstring)}"""', 1)
        else:
            func_str += "..."

        if self.overloads:
            overloads_str = "\n@overload\n".join(str(x) for x in self.overloads)
            func_str = f"@overload\n{func_str}\n@overload\n{overloads_str}"

        return func_str


@dataclass
class Method(Function):
    static: bool = False

    def get_params_str(self) -> str:
        param_str = super().get_params_str()
        if self.static:
            return param_str
        else:
            self_name = "cls" if self.name == "__new__" else "self"
            if param_str:
                return f"{self_name},{param_str}"
            return self_name

    def __str__(self) -> str:
        method_str = ""
        if self.static:
            method_str += "@staticmethod\n"
        method_str += super().__str__()
        return method_str


@dataclass
class Property:
    name: str
    type: str
    default: str | None = None
    docstring: str | None = None

    def __str__(self) -> str:
        prop_str = f"{self.name}:{self.type}"
        if self.default:
            prop_str += f"={self.default}"
        if self.docstring:
            prop_str += f'\n"""{safe_docstring(self.docstring)}"""'
        return prop_str


@dataclass
class PropertyGetSet(Property):
    setter_type: str | None = None
    can_set: bool = False

    def __str__(self) -> str:
        prop_str = "@property"
        prop_str += f"\ndef {self.name}(self)->{self.type}:"
        if self.docstring:
            prop_str += "\n" + indent(f'"""{safe_docstring(self.docstring)}"""', 1)
        else:
            prop_str += "..."

        if self.can_set:
            prop_str += f"\n@{self.name}.setter"
            prop_str += f"\ndef {self.name}(self,value:{self.setter_type or self.type})->None:..."

        return prop_str


@dataclass
class Class:
    ref: type
    name: str
    base_class_names: list[str]
    properties: list[Property]
    methods: list[Method]
    docstring: str | None = None

    def __str__(self) -> str:
        bases_str = f"({','.join(self.base_class_names)})" if self.base_class_names else ""

        class_str = f"class {self.name}{bases_str}:"

        if self.docstring:
            class_str += "\n" + indent(f'"""{safe_docstring(self.docstring)}"""', 1)

        if self.properties:
            props_str = "\n".join(str(prop) for prop in self.properties)
            class_str += f"\n{indent(props_str, 1)}"

        if self.methods:
            method_str = "\n".join(str(method) for method in self.methods)
            class_str += f"\n{indent(method_str.strip(), 1)}"

        if "\n" not in class_str:
            class_str += "..."

        return class_str

    def __lt__(self, other: object) -> bool:
        if not isinstance(other, Class):
            return NotImplemented

        # Check if this class has dependencies on the other class
        if other.name in self.base_class_names:
            return False

        return True
