"""
Formatter for Smart Code Reviewer
Converts raw analyzer output into human-friendly messages
"""
def format_issues(issues, lang="generic"):
    formatted = []

    for line in issues:
        line = line.strip()
        if not line:
            continue

        if lang == "python":
            if "unused-variable" in line:
                formatted.append(f"⚠️ WARNING: Unused variable detected.")
            elif "error" in line.lower():
                formatted.append(f"❌ ERROR: {line}")
            elif "No issues detected" in line:
                formatted.append(f"✅ {line}")
            else:
                formatted.append(f"ℹ️ INFO: {line}")

        elif lang == "javascript":
            if "error" in line.lower():
                formatted.append(f"❌ ERROR: {line}")
            elif "warning" in line.lower():
                formatted.append(f"⚠️ WARNING: {line}")
            elif "No issues detected" in line:
                formatted.append(f"✅ {line}")
            else:
                formatted.append(f"ℹ️ INFO: {line}")

        elif lang == "java":
            if "error" in line.lower():
                formatted.append(f"❌ ERROR: {line}")
            elif "compiled successfully" in line.lower():
                formatted.append(f"✅ {line}")
            else:
                formatted.append(f"ℹ️ INFO: {line}")

        elif lang == "c":
            if "error:" in line.lower():
                msg = line.split("error:")[-1].strip()
                formatted.append(f"❌ ERROR: {msg}")
            elif "warning:" in line.lower():
                msg = line.split("warning:")[-1].strip()
                formatted.append(f"⚠️ WARNING: {msg}")
            elif "compiled successfully" in line.lower():
                formatted.append(f"✅ {line}")
            else:
                formatted.append(f"ℹ️ INFO: {line}")

        else:
            formatted.append(f"ℹ️ INFO: {line}")

    if not formatted:
        formatted.append("ℹ️ No review suggestions found.")

    return formatted
