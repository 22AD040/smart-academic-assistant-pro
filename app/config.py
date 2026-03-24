import os

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

CHUNK_SIZE = 500
CHUNK_OVERLAP = 50
TOP_K = 3
FAISS_PATH = "faiss_index"