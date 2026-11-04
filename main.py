from fastapi import FastAPI

app=FastAPI()

#created an endpoint that runs root function

@app.get("/")

def root():
    return {
        "message":"Welcome To The AI Assistant backend"
    }

@app.get("/about")

def root():
    return {"title":"ai assitant","description":"helps people"}