from dataclasses import dataclass, field


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

    def __str__(self) -> str:
        params_str = ",".join(str(param) for param in self.parameters)

        return_type = self.return_type or "Any"
        func_str = f"def {self.name}({params_str})->{return_type}:"

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
        return prop_str


@dataclass
class Class:
    name: str
    base_classes: list[str]
    properties: list[Property]
    methods: list[Function]
    docstring: str | None = None

    def __str__(self) -> str:
        bases_str = f"({','.join(self.base_classes)})" if self.base_classes else ""

        class_str = f"class {self.name}{bases_str}:\n"

        if self.docstring:
            indented_docstring = "\n\t".join(self.docstring.splitlines())
            class_str += f'\t"""{indented_docstring}"""\n'

        if self.methods:
            funcs_str = "\n\t".join(str(func) for func in self.methods)
            class_str += f"{funcs_str}\n"

        if not self.methods and not self.docstring:
            class_str += "\t..."

        return class_str
