from app.core.vector_store import load_index
from app.config import TOP_K

def retrieve_docs(query):
    db = load_index()
    docs = db.similarity_search(query, k=TOP_K)
    return [d.page_content for d in docs]