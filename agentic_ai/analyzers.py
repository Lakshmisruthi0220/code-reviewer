import os
import subprocess

# ---------- Python ----------
def analyze_python(file_path):
    try:
        result = subprocess.run(
            ["pylint", file_path, "-rn", "--disable=C0114,C0115,C0116"],
            capture_output=True, text=True
        )
        output_lines = result.stdout.splitlines() + result.stderr.splitlines()
        if not output_lines:
            return ["✅ No issues detected. Python code looks clean!"]
        return output_lines
    except FileNotFoundError:
        return ["❌ Pylint not installed. Run: pip install pylint"]

# ---------- JavaScript ----------

# ---------- JavaScript ----------
def analyze_javascript(file_path):
    import subprocess

    try:
        # Run ESLint using npx, each part as a separate list element
        result = subprocess.run(
            ["npx", "eslint", "--no-ignore", "--config", "eslint.config.mjs", file_path],
            capture_output=True, text=True, shell=True
        )
        output_lines = result.stdout.splitlines() + result.stderr.splitlines()
        if not output_lines:
            return ["✅ No issues detected. JS code looks clean!"]
        return output_lines
    except FileNotFoundError:
        return ["❌ ESLint not found. Install locally or globally via npm"]



# ---------- Java ----------
def analyze_java(file_path):
    try:
        result = subprocess.run(
            ["javac", file_path],
            capture_output=True, text=True
        )
        output_lines = result.stderr.splitlines() + result.stderr.splitlines()
        if not output_lines:
            return ["✅ No issues detected. Java code compiled successfully!"]
        return output_lines
    except FileNotFoundError:
        return ["❌ Java compiler not found. Install JDK."]

# ---------- C ----------
def analyze_c(file_path):
    try:
        result = subprocess.run(
            ["gcc", "-Wall", "-fsyntax-only", file_path],
            capture_output=True, text=True
        )
        output_lines = result.stderr.splitlines() + result.stderr.splitlines()
        if not output_lines:
            return ["✅ No issues detected. C code compiled successfully!"]
        return output_lines
    except FileNotFoundError:
        return ["❌ GCC not found. Install MinGW or MSYS2."]
