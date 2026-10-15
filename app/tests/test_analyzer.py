from app.analyzer import analyze_code


def test_analyze_function():
    result = analyze_code("def hello():\n    return 'Hello'")

    assert result["success"] is True
    assert "hello" in result["functions"]


def test_analyze_class():
    result = analyze_code("class Student:\n    pass")

    assert result["success"] is True
    assert "Student" in result["classes"]


def test_detect_syntax_error():
    result = analyze_code("def hello(:")

    assert result["success"] is False
    assert result["line"] == 1


def test_detect_todo_comment():
    result = analyze_code("# TODO: fix this")

    assert result["success"] is True
    assert len(result["issues"]) > 0