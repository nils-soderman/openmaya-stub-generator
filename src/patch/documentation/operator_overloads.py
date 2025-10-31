import enum
import re

from ...stub_types import Class, Method, Parameter
from .parser.interface import NumberSupport, Page
from . import convert_type


class EOperatorType(enum.Enum):
    LEFT_SIDE = enum.auto()
    RIGHT_SIDE = enum.auto()
    INPLACE = enum.auto()


OPERATOR_OVERLOAD_MAP = {
    # Method (Operator, OperatorType)
    "__xor__": ("^", EOperatorType.LEFT_SIDE),
    "__rxor__": ("^", EOperatorType.RIGHT_SIDE),
    "__ixor__": ("^", EOperatorType.INPLACE),

    "__mul__": ("*", EOperatorType.LEFT_SIDE),
    "__rmul__": ("*", EOperatorType.RIGHT_SIDE),
    "__imul__": ("*", EOperatorType.INPLACE),

    "__add__": ("+", EOperatorType.LEFT_SIDE),
    "__radd__": ("+", EOperatorType.RIGHT_SIDE),
    "__iadd__": ("+", EOperatorType.INPLACE),

    "__sub__": ("-", EOperatorType.LEFT_SIDE),
    "__rsub__": ("-", EOperatorType.RIGHT_SIDE),
    "__isub__": ("-", EOperatorType.INPLACE),

    "__truediv__": ("/", EOperatorType.LEFT_SIDE),
    "__rtruediv__": ("/", EOperatorType.RIGHT_SIDE),
    "__itruediv__": ("/", EOperatorType.INPLACE),
}


def get_matching_operators(class_name: str, operator_overloads_list: list[NumberSupport], operator: str, operator_type: EOperatorType) -> list[NumberSupport]:
    escaped_operator = re.escape(operator)
    if operator_type == EOperatorType.LEFT_SIDE:
        # e.g. MVector = MVector * float
        pattern = rf"=\s*{class_name}\s*{escaped_operator}\s*\w+"
    elif operator_type == EOperatorType.RIGHT_SIDE:
        # e.g. MVector = float * MVector
        pattern = rf"=\s*\w+\s*{escaped_operator}\s*{class_name}"
    else:  # INPLACE
        # e.g. MVector *= Scalar
        pattern = rf"{class_name}\s*{escaped_operator}="

    if RetunValue := [x for x in operator_overloads_list if re.search(pattern, x.operation)]:
        return RetunValue

    # Try to match without the equals, if it's documented as 'MColor * float' instead of 'MColor = MColor * float'
    if operator_type == EOperatorType.LEFT_SIDE:
        pattern = rf"{class_name}\s*{escaped_operator}\s*\w+"
    elif operator_type == EOperatorType.RIGHT_SIDE:
        pattern = rf"\w+\s*{escaped_operator}\s*{class_name}"
    else:  # INPLACE
        return []

    return [x for x in operator_overloads_list if re.search(pattern, x.operation)]


def process_operator_overloads(class_: Class, method: Method, class_doc: Page) -> None:
    if not class_doc.detailed_description:
        return

    operator_info = OPERATOR_OVERLOAD_MAP.get(method.name)
    if not operator_info:
        return

    operator, operator_type = operator_info

    matching_operators = get_matching_operators(class_.name,
                                                class_doc.detailed_description.number_support,
                                                operator,
                                                operator_type)

    for i, matching_operator in enumerate(matching_operators):
        if i > 0:
            # Create a new overload method
            new_method = Method(method.ref,
                                method.name,
                                return_type="Any",
                                docstring=method.docstring,
                                deprecated=method.deprecated,
                                static=method.static)
            method.overloads.append(new_method)
        else:
            new_method = method

        new_method.docstring = matching_operator.description

        if "=" in matching_operator.operation:
            return_value, _, operational_str = matching_operator.operation.partition('=')
        else:
            # If documented without '=' ('MColor * float'), assume the return type is the class itself
            return_value = class_.name
            operational_str = matching_operator.operation

        type_1, _, type_2 = operational_str.partition(operator)
        type_1 = type_1.strip()
        type_2 = type_2.strip()

        type_other = type_2 if (type_2 and type_2 != class_.name) else type_1

        if operator_type == EOperatorType.INPLACE:
            new_method.return_type = "Self"
        else:
            new_method.return_type = convert_type.get_python_type_from_desc(return_value.strip())

        new_method.parameters = [
            Parameter(
                name="other",
                type=convert_type.get_python_type_from_desc(type_other),
            )
        ]
