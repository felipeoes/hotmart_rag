import uvicorn
from fastapi import FastAPI
from routers import chat
from config import RAG_LLM_FASTAPI_PORT, RAG_LLM_FASTAPI_HOST

app = FastAPI()
app.include_router(chat.router)

@app.get("/healthcheck")
async def healthcheck():
    return {"status": "ok"}


if __name__ == "__main__":
    uvicorn.run(app, port=RAG_LLM_FASTAPI_PORT, host=RAG_LLM_FASTAPI_HOST if RAG_LLM_FASTAPI_HOST else "0.0.0.0")
