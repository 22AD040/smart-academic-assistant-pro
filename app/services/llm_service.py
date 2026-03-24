from langchain_google_genai import ChatGoogleGenerativeAI
from app.config import GEMINI_API_KEY

llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    google_api_key=GEMINI_API_KEY,
    temperature=0.3
)

def get_answer(query, context=None):

    if context:
        prompt = f"""
You are an advanced academic AI assistant.

STRICT RULES:
- Give LONG structured answers
- Use clear headings
- Use bullet points
- Give examples
- Be accurate
- No hallucination
- Generate Key Points
- Generate Mindmap (text format)

IMPORTANT:
- Answer ONLY from the given PDF context
- If not found → say "Not found in PDF"

Context:
{context}

Question:
{query}
"""
    else:
        prompt = f"""
You are an advanced academic AI assistant.

STRICT RULES:
- Give LONG structured answers
- Use clear headings
- Use bullet points
- Give examples
- Be accurate
- No hallucination
- Generate Key Points
- Generate Mindmap (text format)

Question:
{query}
"""

    response = llm.invoke(prompt)
    return response.content