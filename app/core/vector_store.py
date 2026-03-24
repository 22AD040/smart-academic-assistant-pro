import os
from langchain_community.vectorstores import FAISS
from app.core.embeddings import get_embedding_model
from app.config import FAISS_PATH


def save_index(chunks):
    embeddings = get_embedding_model()

    db = FAISS.from_texts(chunks, embeddings)

    os.makedirs(FAISS_PATH, exist_ok=True)
    db.save_local(FAISS_PATH)


def load_index():
    embeddings = get_embedding_model()

    if not os.path.exists(FAISS_PATH):
        raise Exception("⚠️ FAISS index not found. Run build_index.py first")

    db = FAISS.load_local(
        FAISS_PATH,
        embeddings,
        allow_dangerous_deserialization=True
    )

    return db