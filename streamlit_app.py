import streamlit as st
from typing import Generator
from groq import Groq

st.set_page_config(page_icon="💬", layout="wide",
                   page_title="File upload..")


def icon(emoji: str):
    """Shows an emoji as a Notion-style page icon."""
    st.write(
        f'<span style="font-size: 78px; line-height: 1">{emoji}</span>',
        unsafe_allow_html=True,
    )


icon("🏎️")

st.subheader("Groq Chat Streamlit App", divider="rainbow", anchor=False)

# Set the maximum file size to 4GB
MAX_FILE_SIZE = 4 * (1024 ** 3)  # 4GB

# Create a Streamlit app
st.title("File Uploader")
st.write("Upload a file (max 4GB)")

# Create a file uploader widget
uploaded_file = st.file_uploader("Select a file to upload", type=[""], accept_multiple_files=False)

# Check if a file has been uploaded
if uploaded_file:
    # Check if the file size exceeds the maximum allowed size
    if uploaded_file.size > MAX_FILE_SIZE:
        st.error("File too large. Maximum allowed size is 4GB.")
    else:
        # Process the uploaded file
        st.write("File uploaded successfully!")
        # You can add additional code here to process the uploaded file
        # For example, you can save the file to a database or perform some analysis on it
