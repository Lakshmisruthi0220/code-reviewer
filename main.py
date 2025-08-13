"""
Smart Code Reviewer - Multi-language
Developed with Cursor AI + Agentic AI principles
"""

import sys
from agentic_ai.agent import review_code

def main():
    if len(sys.argv) < 2:
        print("Usage: python main.py <file_path>")
        return

    file_path = sys.argv[1]
    feedback = review_code(file_path)

    print("\n--- CODE REVIEW REPORT ---")
    for line in feedback:
        print(line)

if __name__ == "__main__":
    main()
