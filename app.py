


import streamlit as st
import tempfile
import os
from dotenv import load_dotenv
from utils import extract_text_from_pdf, chunk_text
from generator import generate_flashcards
import openai  # Add this import

# Load environment variables
load_dotenv()

# Configure OpenAI with your API key
openai.api_key = os.getenv("OPENAI_API_KEY")  # This uses the key from .env

# Page config
st.set_page_config(page_title="📚 AI Flashcard Generator", layout="centered")
st.title("📚 AI Flashcard Generator")

# Sidebar settings
st.sidebar.header("⚙️ Flashcard Settings")
num_flashcards = st.sidebar.slider("Number of Flashcards", 5, 50, 10)
question_type = st.sidebar.selectbox("Format", ["Q&A", "True/False", "MCQ"])

# File uploader
uploaded_file = st.file_uploader("Upload PDF", type=["pdf"])

if uploaded_file:
    with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp:
        tmp.write(uploaded_file.read())
        text = extract_text_from_pdf(tmp.name)

    if text:
        with st.spinner("Generating flashcards..."):
            chunks = chunk_text(text)
            flashcards = generate_flashcards(
                chunks,
                num=num_flashcards,
                question_type=question_type
            )

        # Display flashcards
        for i, (q, a) in enumerate(flashcards, 1):
            st.markdown(f"""
            <div style='border:1px solid #ddd; padding:10px; margin:10px; border-radius:5px;'>
                <b>Q{i}:</b> {q}<br><br>
                <details><summary>Answer</summary>{a}</details>
            </div>
            """, unsafe_allow_html=True)
    else:
        st.warning("No text extracted from PDF.")
else:
    st.info("Upload a PDF to begin")
