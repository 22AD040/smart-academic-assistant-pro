from pypdf import PdfReader
import os
from app.config import CHUNK_SIZE, CHUNK_OVERLAP


def extract_text(file_path):


    if os.path.getsize(file_path) == 0:
        raise ValueError("❌ PDF file is empty")

    reader = PdfReader(file_path)
    text = ""

    for i, page in enumerate(reader.pages):
        try:
            content = page.extract_text()
            if content:
                text += f"\n[Page {i+1}]\n{content}"
        except:
            continue

    return text


def chunk_text(text, chunk_size=500, overlap=50):
    chunks = []
    start = 0

    while start < len(text):
        end = start + chunk_size
        chunk = text[start:end]
        chunks.append(chunk)

        start += chunk_size - overlap

    return chunks