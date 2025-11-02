
from src.patch.documentation.parser.signature import extract_signatures_from_docstring, parse_signature, ParsedSignature, SignatureParameter


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

    docstring = """addPolyComponentIdChangedCallback(node, (wantVertIds, wantEdgeIds, wantFaceIds), function, clientData=None) -> id"""
    signatures = extract_signatures_from_docstring(docstring, "addPolyComponentIdChangedCallback")
    assert signatures == [
        "addPolyComponentIdChangedCallback(node, (wantVertIds, wantEdgeIds, wantFaceIds), function, clientData=None) -> id"
    ]


def test_parse_signature():
    result = parse_signature("reparentNode(node, newParent=MObject.kNullObj)")
    assert result == ParsedSignature(
        return_type=None,
        parameters=[
            SignatureParameter("node", None, None),
            SignatureParameter("newParent", None, "MObject.kNullObj"),
        ]
    )

    result = parse_signature("example(node, lineColor=MColor(1, 1, 1))")
    assert result == ParsedSignature(
        return_type=None,
        parameters=[
            SignatureParameter("node", None, None),
            SignatureParameter("lineColor", None, "MColor(1, 1, 1)"),
        ]
    )

    result = parse_signature("addPolyComponentIdChangedCallback(node, (wantVertIds, wantEdgeIds, wantFaceIds), function, clientData=None) -> id")
    assert result == ParsedSignature(
        return_type="id",
        parameters=[
            SignatureParameter("node", None, None),
            SignatureParameter("arg", "(wantVertIds, wantEdgeIds, wantFaceIds)", None),
            SignatureParameter("function", None, None),
            SignatureParameter("clientData", None, "None"),
        ]
    )
