


import streamlit as st
import tempfile
import os
from dotenv import load_dotenv
from utils import extract_text_from_pdf, chunk_text
from generator import generate_flashcards

# Load environment variables
load_dotenv()

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
#2


# import streamlit as st
# import tempfile
# import streamlit.components.v1 as components

# from utils import extract_text_from_pdf, chunk_text
# from generator import generate_flashcards, load_question_generator  # Make sure these are updated

# # Page configuration
# st.set_page_config(page_title="📚 AI Flashcard Generator", layout="centered")
# st.title("📚 AI Flashcard Generator")

# # Sidebar for flashcard settings
# st.sidebar.header("⚙️ Flashcard Settings")
# num_flashcards = st.sidebar.slider("Number of Flashcards", min_value=5, max_value=50, value=10)
# complexity = st.sidebar.selectbox("Question Complexity", ["Basic", "Intermediate", "Detailed"])
# chunk_size = st.sidebar.slider("Max Chunk Size (in characters)", min_value=100, max_value=1000, value=300)
# question_type = st.sidebar.selectbox("Flashcard Format", ["Q&A", "Fill in the Blanks", "True/False", "MCQ"])

# # Option to choose input method
# input_method = st.radio("Choose Input Method", ["Upload PDF", "Paste Plain Text"])

# text = ""

# if input_method == "Upload PDF":
#     uploaded_file = st.file_uploader("Upload a PDF file", type=["pdf"])
#     if uploaded_file is not None:
#         with st.spinner("Extracting text from PDF..."):
#             with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp:
#                 tmp.write(uploaded_file.read())
#                 tmp_path = tmp.name
#             text = extract_text_from_pdf(tmp_path)

# elif input_method == "Paste Plain Text":
#     text = st.text_area("Paste or type your text below:", height=300)

# # If text exists, generate flashcards
# if text.strip():
#     with st.spinner("Generating flashcards..."):
#         chunks = chunk_text(text, max_len=chunk_size)

#         # Load T5 model (only for Q&A)
#         model_tokenizer = None
#         if question_type == "Q&A":
#             model_tokenizer = load_question_generator()

#         flashcards = generate_flashcards(
#             chunks,
#             num=num_flashcards,
#             complexity=complexity,
#             question_type=question_type,
#             model_tokenizer=model_tokenizer
#         )

#     # Display flashcards as flip-cards
#     if flashcards:
#         st.success(f"Generated {len(flashcards)} flashcards!")
#         for i, (q, a) in enumerate(flashcards, 1):
#             components.html(f"""
#             <div style="perspective: 1000px; margin-bottom: 30px;">
#               <div style="width: 100%; max-width: 500px; margin: auto; height: 250px; position: relative; transition: transform 0.8s; transform-style: preserve-3d; cursor: pointer;"
#                    onclick="this.style.transform = this.style.transform === 'rotateY(180deg)' ? 'rotateY(0deg)' : 'rotateY(180deg)'">
#                 <div style="position: absolute; width: 100%; height: 100%; backface-visibility: hidden; background-color: #f0f2f6; display: flex; align-items: center; justify-content: center; border: 2px solid #ccc; border-radius: 15px; padding: 20px; overflow: auto;">
#                   <strong>Q{i}:</strong>&nbsp;{q}
#                 </div>
#                 <div style="position: absolute; width: 100%; height: 100%; backface-visibility: hidden; background-color: #d9fdd3; color: black; transform: rotateY(180deg); display: flex; align-items: center; justify-content: center; border: 2px solid #ccc; border-radius: 15px; padding: 20px; overflow: auto;">
#                   <strong>A{i}:</strong>&nbsp;{a}
#                 </div>
#               </div>
#             </div>
#             """, height=300)
#     else:
#         st.warning("No flashcards could be generated.")
# else:
#     st.info("📄 Please upload a PDF or enter text to get started.")




