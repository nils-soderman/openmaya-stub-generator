from dataclasses import dataclass, field


def indent(code: str, num: int) -> str:
    indent_str = '\t' * num
    return indent_str + "\n".join(
        f"{indent_str}{line.rstrip()}" if line.strip() else ""
        for line in code.splitlines()
    ).lstrip()


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
        if self.default:
            param_str += f"={self.default}"
        return param_str


@dataclass
class Function:
    name: str
    return_type: str | None = None
    parameters: list[Parameter] = field(default_factory=list)
    docstring: str | None = None
    bStatic: bool = False

    def __str__(self) -> str:
        func_str = ""

        if self.bStatic:
            func_str += "@staticmethod\n"

        params_str = ",".join(str(param) for param in self.parameters)
        return_type = self.return_type or "Any"

        func_str += f"def {self.name}({params_str})->{return_type}:"

        if self.docstring:
            func_str += f'\n\t"""{self.docstring}"""'
        else:
            func_str += "..."

        return func_str


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
            prop_str += f'\n"""{self.docstring}"""'
        return prop_str


@dataclass
class PropertyGetSet(Property):
    setter_type: str | None = None
    can_set: bool = False

    def __str__(self) -> str:
        prop_str = "@property"
        prop_str += f"\ndef {self.name}(self)->{self.type}:"
        if self.docstring:
            prop_str += "\n" + indent(f'"""{self.docstring}"""', 1)
        else:
            prop_str += "..."

        if self.can_set:
            prop_str += f"\n@{self.name}.setter"
            prop_str += f"\ndef {self.name}(self,value:{self.setter_type or self.type})->None:..."

        return prop_str


@dataclass
class Class:
    name: str
    base_class_names: list[str]
    properties: list[Property]
    methods: list[Function]
    docstring: str | None = None

    def __str__(self) -> str:
        bases_str = f"({','.join(self.base_class_names)})" if self.base_class_names else ""

        class_str = f"class {self.name}{bases_str}:"

        if self.docstring:
            class_str += "\n" + indent(f'"""{self.docstring}"""', 1)

        if self.properties:
            props_str = "\n".join(str(prop) for prop in self.properties)
            class_str += f"\n{indent(props_str, 1)}"

        if self.methods:
            funcs_str = "\n".join(str(func) for func in self.methods)
            class_str += f"\n{indent(funcs_str, 1)}"

        if "\n" not in class_str:
            class_str += "..."

        return class_str
