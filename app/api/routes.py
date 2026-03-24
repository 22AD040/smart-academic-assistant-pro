from fastapi import APIRouter, UploadFile, File
from pydantic import BaseModel
from app.services.llm_service import get_answer
from app.core.retrieval import retrieve_docs
from scripts.build_index import build_from_pdf
import os

router = APIRouter()



class Query(BaseModel):
    question: str



@router.get("/")
def home():
    return {"message": "API running"}



@router.post("/ask")
def ask(query: Query):
    question = query.question


    if os.path.exists("faiss_index/index.faiss"):

        docs = retrieve_docs(question)

        if docs:
            context = "\n".join(docs)

            answer = get_answer(question, context)

            # 🔥 NEW FIX: CHECK IF NOT FOUND
            if "Not found in PDF" not in answer:
                return {
                    "answer": "📄 Based on uploaded PDF:\n\n" + answer
                }


    answer = get_answer(question)

    return {
        "answer": "🧠 Based on general knowledge:\n\n" + answer
    }



@router.post("/build")
async def build_index(file: UploadFile = File(...)):
    try:

        if os.path.exists("faiss_index/index.faiss"):
            return {"message": "⚡ Index already exists (Skipping rebuild)"}


        file_path = f"temp_{file.filename}"

        with open(file_path, "wb") as f:
            f.write(await file.read())


        build_from_pdf(file_path)

        return {"message": "✅ PDF indexed successfully"}

    except Exception as e:
        return {"error": str(e)}



@router.post("/reset")
def reset_index():
    try:
        if os.path.exists("faiss_index"):
            import shutil
            shutil.rmtree("faiss_index")
            return {"message": "✅ Index deleted"}
        return {"message": "No index found"}
    except Exception as e:
        return {"error": str(e)}