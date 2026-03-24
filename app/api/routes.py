from fastapi import APIRouter, UploadFile, File
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from app.services.llm_service import get_answer
from app.core.retrieval import retrieve_docs
import os
import traceback

router = APIRouter()


class Query(BaseModel):
    question: str


# ✅ ROOT (IMPORTANT for UptimeRobot)
@router.get("/")
def home():
    return {"status": "ok", "message": "Backend is running"}


# ✅ ALSO SUPPORT HEAD (VERY IMPORTANT)
@router.head("/")
def head_home():
    return {"status": "ok"}


# ✅ ASK API
@router.post("/ask")
def ask(query: Query):
    question = query.question

    if os.path.exists("faiss_index/index.faiss"):
        docs = retrieve_docs(question)

        if docs:
            context = "\n".join(docs)
            answer = get_answer(question, context)

            if "Not found in PDF" not in answer:
                return {
                    "answer": "📄 Based on uploaded PDF:\n\n" + answer
                }

    answer = get_answer(question)

    return {
        "answer": "🧠 Based on general knowledge:\n\n" + answer
    }


# ✅ BUILD API (FIXED)
@router.post("/build")
async def build_index(file: UploadFile = File(...)):
    try:
        contents = await file.read()

        with open("temp.pdf", "wb") as f:
            f.write(contents)

        from app.core.vector_store import build_vector_store

        build_vector_store("temp.pdf")

        return {"status": "success"}

    except Exception as e:
        print(traceback.format_exc())
        return JSONResponse(
            status_code=500,
            content={"error": str(e)}
        )


# ✅ RESET
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