import sys
import os


sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from app.utils.pdf_utils import extract_text, chunk_text
from app.core.vector_store import save_index


PDF_PATH = "ai_notes.pdf"


def run():
    if not os.path.exists(PDF_PATH):
        print(f"❌ File not found: {PDF_PATH}")
        return

    text = extract_text(PDF_PATH)
    chunks = chunk_text(text)
    save_index(chunks)

    print("✅ Default PDF Index Ready!")



def build_from_pdf(file_path):
    if not os.path.exists(file_path):
        print(f"❌ File not found: {file_path}")
        return

    text = extract_text(file_path)
    chunks = chunk_text(text)
    save_index(chunks)

    print("✅ Uploaded PDF Index Ready!")



if __name__ == "__main__":
    run()