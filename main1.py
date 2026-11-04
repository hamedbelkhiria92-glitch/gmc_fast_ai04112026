from fastapi import FastAPI
from pydantic import BaseModel,Field
class ChatRequest(BaseModel):
    message:str
class QuizzRequest(BaseModel):
    subject:str = Field(...,min_length=3)
    number_quizzes : int = Field(...,lt=10,gt=1)
    number_options : int = Field(...,gt=2,lt=5)
app = FastAPI()
# Created an endpoint that runs root function
@app.get("/")
def root():
    return {
        "status":"ok",
        "message":"Welcome To the AI Assistant backend"
    }
@app.get("/about")
def about():
    return {
        "status":"ok",
        "Title":"AI Student assistant",
        "Description":"it helps students"
    }
@app.get("/health")
def health():
    return {
        "status":"ok","version":"0.1.0"
    }
@app.post("/chat")
def chat(request:ChatRequest):
    return {
        "answer":f"You asked for {request.message}",
        "model":"placeholder",
        "tokens":0
    }
@app.post("/quizz")
def quizz(request:QuizzRequest):
    return {
        "topic":f"{request.subject}",
        "quizzes":[
            {
                "question":"fkdjkfdl",
                "options":["dfjkdhf","dfhkdj","fdjhdf","fjhkjd"],
                "correct_answer":0
            }
        ]
    }

class SummarizeQuest1(BaseModel):
    request:str
@app.get("/summarize1")
def summarize(request:SummarizeQuest1):
    return {summarize:request}

class FlashCard1(BaseModel):
    flash:str

app.get("/flashcard1")
def flashcard(request:FlashCard1):
    return {flashcard:request}


class SummarizeQuest(BaseModel):
    topic:str
@app.post("/summarize")
def summarize(request:SummarizeQuest):
    return {"topic":request.topic,
            "summary":"This is summary"}

class FlashCard(BaseModel):
    cours:str
    number_flashcards:int

app.get("/flashcard")
def flashcard(request:FlashCard):
    return {"topic":request.topic,
            "flashcards":["a","b","c"]}