
from src.patch.documentation.parser.signature import extract_signatures_from_docstring


def test_extract_signatures_from_docstring():
    docstring = """
    sample_function(param1: int, param2: str) -> bool
    sample_function(param1: int)

    Some text here, this should break the parsing.

    sample_function()
    """

    signatures = extract_signatures_from_docstring(docstring, "sample_function")
    assert signatures == [
        "sample_function(param1: int, param2: str) -> bool",
        "sample_function(param1: int)"
    ]

    signatures = extract_signatures_from_docstring(docstring, "sample_function", stop_search_at_text=False)
    assert signatures == [
        "sample_function(param1: int, param2: str) -> bool",
        "sample_function(param1: int)",
        "sample_function()"
    ]

    # signatures might be split over multiple lines
    docstring = """
    connect(MPlug source, MPlug dest) -> self
    connect(MObject sourceNode, MObject sourceAttr,
            MObject destNode,   MObject destAttr) -> self
    """
    signatures = extract_signatures_from_docstring(docstring, "connect")
    assert signatures == [
        "connect(MPlug source, MPlug dest) -> self",
        "connect(MObject sourceNode, MObject sourceAttr,            MObject destNode,   MObject destAttr) -> self"
    ]

    # Some docstrings are broken and have multiple signatures without separation
    docstring = """sample_function(param1: int, param2: str) -> boolsample_function(param1: int)
    Some text here, this should break the parsing.
    """
    signatures = extract_signatures_from_docstring(docstring, "sample_function")
    assert signatures == [
        "sample_function(param1: int, param2: str) -> bool",
        "sample_function(param1: int)"
    ]

    # Function Name appears as a argument
    docstring = """setAngle(index, setAngle, isInTangent, change=None) -> self"""
    signatures = extract_signatures_from_docstring(docstring, "setAngle")
    assert signatures == [
        "setAngle(index, setAngle, isInTangent, change=None) -> self"
    ]

    docstring = """create(cvs, knots, degree, form, is2D, rational, parent=kNullObj)
-> self
create(subCurves, parent=kNullObj) -> self"""

    signatures = extract_signatures_from_docstring(docstring, "create")
    assert signatures == [
        "create(cvs, knots, degree, form, is2D, rational, parent=kNullObj)-> self",
        "create(subCurves, parent=kNullObj) -> self"
    ]