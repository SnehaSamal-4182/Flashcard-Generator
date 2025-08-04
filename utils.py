<<<<<<< HEAD
# # utils.py

# import pdfplumber
# import nltk
# nltk.download('punkt')
# from nltk.tokenize import sent_tokenize

# def extract_text_from_pdf(pdf_path):
#     text = ""
#     with pdfplumber.open(pdf_path) as pdf:
#         for page in pdf.pages:
#             text += page.extract_text() + "\n"
#     return text

# def chunk_text(text, max_len=300):
#     sentences = sent_tokenize(text)
#     chunks, chunk = [], ""
#     for sentence in sentences:
#         if len(chunk) + len(sentence) <= max_len:
#             chunk += sentence + " "
#         else:
#             chunks.append(chunk.strip())
#             chunk = sentence + " "
#     if chunk:
#         chunks.append(chunk.strip())
#     return chunks


import pdfplumber
import re

def extract_text_from_pdf(pdf_path):
    """Extracts all text from a given PDF file using pdfplumber."""
    text = ""
    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            page_text = page.extract_text()
            if page_text:
                text += page_text + "\n"
    return text.strip()

def basic_sentence_tokenizer(text):
    """Splits text into sentences using regex (approximate but effective)."""
    sentence_endings = re.compile(r'(?<=[.!?])\s+')
    return sentence_endings.split(text)

def chunk_text(text, max_len=300):
    """Splits text into sentence chunks not exceeding max_len characters."""
    sentences = basic_sentence_tokenizer(text)
    chunks = []
    chunk = ""

    for sentence in sentences:
        if len(chunk) + len(sentence) <= max_len:
            chunk += sentence + " "
        else:
            chunks.append(chunk.strip())
            chunk = sentence + " "

    if chunk:
        chunks.append(chunk.strip())

    return chunks
=======



import pdfplumber
import re

def extract_text_from_pdf(pdf_path):
    """Extracts all text from a given PDF file using pdfplumber."""
    text = ""
    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            page_text = page.extract_text()
            if page_text:
                text += page_text + "\n"
    return text.strip()

def basic_sentence_tokenizer(text):
    """Splits text into sentences using regex (approximate but effective)."""
    sentence_endings = re.compile(r'(?<=[.!?])\s+')
    return sentence_endings.split(text)

def chunk_text(text, max_len=300):
    """Splits text into sentence chunks not exceeding max_len characters."""
    sentences = basic_sentence_tokenizer(text)
    chunks = []
    chunk = ""

    for sentence in sentences:
        if len(chunk) + len(sentence) <= max_len:
            chunk += sentence + " "
        else:
            chunks.append(chunk.strip())
            chunk = sentence + " "

    if chunk:
        chunks.append(chunk.strip())

    return chunks

>>>>>>> d6512ef46fed49a333187fbdccc55a6cffcc0ec0
