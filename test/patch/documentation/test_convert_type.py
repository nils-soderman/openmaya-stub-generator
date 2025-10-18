# test_convert_type.py
from src.patch.documentation.convert_type import (get_python_type_from_desc,
                                                  split_outside_nested)


def test_split_outside_nested():
    assert split_outside_nested("abc(123) HelloWorld", ",", "(", ")") == ["abc(123) HelloWorld"]
    assert split_outside_nested("a, b or c", [",", " or "], "(", ")") == ["a", "b", "c"]
    assert split_outside_nested("or(arg1,arg2),arg3", [",", " or "], "(", ")") == ["or(arg1,arg2)", "arg3"]
    assert split_outside_nested("a, func(b, c) or [x, y]", [",", " or "], "([", ")]") == ['a', 'func(b, c)', '[x, y]']


def test_get_python_type_from_desc():
    assert get_python_type_from_desc("string") == "str"
    assert get_python_type_from_desc("MAngle , MDistance or MTime") == "MAngle|MDistance|MTime"
    assert get_python_type_from_desc("Angular unit type constant") == "int"
    assert get_python_type_from_desc("tuple of strings") == "tuple[str, ...]"
