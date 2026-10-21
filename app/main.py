from fastapi import FastAPI

app = FastAPI(
    title="REELS AI COACH",
    description="인스타그램 릴스 기획과 대본 작성을 돕는 AI 챗봇",
    version="0.1.0",
)


@app.get("/health")
def health():
    return {
        "status": "ok",
        "service": "reels-ai-coach",
    }