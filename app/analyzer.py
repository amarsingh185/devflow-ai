import ast


def analyze_code(code: str) -> dict:
    try:
        tree = ast.parse(code)

        functions = [
            node.name
            for node in ast.walk(tree)
            if isinstance(
                node,
                (ast.FunctionDef, ast.AsyncFunctionDef)
            )
        ]

        classes = [
            node.name
            for node in ast.walk(tree)
            if isinstance(node, ast.ClassDef)
        ]

        issues = []
        lines = code.splitlines()

        # Check for long lines
        for line_number, line in enumerate(lines, start=1):
            if len(line) > 88:
                issues.append({
                    "line": line_number,
                    "issue": "Line is longer than 88 characters"
                })

        # Check for TODO comments
        for line_number, line in enumerate(lines, start=1):
            if "TODO" in line:
                issues.append({
                    "line": line_number,
                    "issue": "TODO comment found"
                })

        return {
            "success": True,
            "lines": len(lines),
            "functions": functions,
            "classes": classes,
            "issues": issues,
            "message": "Code analysis completed successfully."
        }

    except SyntaxError as error:
        return {
            "success": False,
            "error": error.msg,
            "line": error.lineno,
            "message": "Python syntax error found."
        }