from fastapi import FastAPI
from pydantic import BaseModel

from app.analyzer import analyze_code

app = FastAPI(
    title="DevFlow AI",
    description="AI-Powered Software Engineering Platform",
    version="0.2.0"
)


class CodeRequest(BaseModel):
    code: str


@app.get("/")
def home():
    return {
        "project": "DevFlow AI",
        "message": "Welcome to DevFlow AI!",
        "status": "running"
    }


@app.post("/analyze")
def code_analysis(request: CodeRequest):
    result = analyze_code(request.code)
    return result