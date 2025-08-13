import os
from agentic_ai import analyzers, formatter
from cursor_ai.suggester import generate_suggestions

def review_code(file_path):
    """Review a single file and return issues + suggestions"""
    ext = os.path.splitext(file_path)[1].lower()
    if ext == ".py":
        language = "python"
        issues = analyzers.analyze_python(file_path)
    elif ext == ".js":
        language = "javascript"
        issues = analyzers.analyze_javascript(file_path)
    elif ext == ".java":
        language = "java"
        issues = analyzers.analyze_java(file_path)
    elif ext == ".c":
        language = "c"
        issues = analyzers.analyze_c(file_path)
    else:
        return ["Unsupported file type"]

    # Cursor AI suggestions
    with open(file_path, "r") as f:
        code = f.read()
    suggestions = generate_suggestions(code, language)

    # Format combined output
    return formatter.format_issues(issues) + suggestions
