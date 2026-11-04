from fastapi import FastAPI
from test import ChatRequest

app = FastAPI()

# created an endpoint that runs root function

@app.get("/")
def root():
    return {
        "message": "Welcome To The AI Assistant backend"
    }

@app.get("/about")
def about():
    return {"title": "ai assitant", "description": "helps people"}

@app.get("/health")
def health():
    return {
        "health": "good"
    }

@app.post("/chat")
def chat(request: ChatRequest):
    return {
        "answer": f"You asked for {request.message}",
        "model": "placeholder",
        "tokens": 0
    }


 