"""
Local Cursor AI module for generating suggestions.
"""

def generate_suggestions(code, language):
    """
    Return a list of suggested improvements for given code.
    For now, it uses simple rules; can be extended with Cursor AI templates.
    """
    suggestions = []

    if language == "python":
        if "print(" in code:
            suggestions.append("Consider using logging instead of print for production code")
        if "def " in code and "docstring" not in code:
            suggestions.append("Add docstrings for all functions")
    elif language == "javascript":
        if ";" not in code:
            suggestions.append("Add missing semicolons")
        if "var " in code:
            suggestions.append("Consider using let or const instead of var")
    elif language == "java":
        suggestions.append("Ensure proper exception handling and semicolons")
    elif language == "c":
        suggestions.append("Check variable declarations and semicolons")
    return suggestions
