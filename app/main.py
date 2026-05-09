from fastapi import FastAPI
from app.models import ChatRequest
from app.agent import generate_reply

app = FastAPI()


@app.get("/health")
def health():

    return {
        "status": "ok"
    }


@app.post("/chat")
def chat(request: ChatRequest):

    response = generate_reply(
        request.messages
    )

    return response

