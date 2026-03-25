from fastapi import APIRouter
from pydantic import BaseModel
from app.services.llm_service import get_answer

router = APIRouter()


class Query(BaseModel):
    question: str


@router.get("/")
def home():
    return {"message": "API running"}


@router.post("/ask")
def ask(query: Query):
    question = query.question


    answer = get_answer(question)

    return {
        "answer": "🧠 " + answer
    }