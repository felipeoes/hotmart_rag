import uvicorn
from fastapi import FastAPI
from routers import chat
from config import FASTAPI_PORT, FASTAPI_HOST

app = FastAPI()
app.include_router(chat.router)

@app.get("/healthcheck")
async def healthcheck():
    return {"status": "ok"}


if __name__ == "__main__":
    uvicorn.run(app, port=FASTAPI_PORT, host=FASTAPI_HOST)
