import streamlit as st
from agentic_ai.agent import review_code
import os

st.title("Smart Code Reviewer")

# Create temp folder if it doesn't exist
os.makedirs("temp", exist_ok=True)

uploaded_files = st.file_uploader(
    "Upload your code files (PY, JS, JAVA, C) or multiple files",
    type=["py", "js", "java", "c"],
    accept_multiple_files=True
)

if uploaded_files:
    for uploaded_file in uploaded_files:  # Loop through each uploaded file
        file_path = os.path.join("temp", uploaded_file.name)
        with open(file_path, "wb") as f:
            f.write(uploaded_file.getbuffer())

        st.info(f"File uploaded: {uploaded_file.name}")

        # Run Agentic AI review
        st.write("Running code review...")
        feedback = review_code(file_path)
        st.text("\n".join(feedback))