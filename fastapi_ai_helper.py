from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class TopicRequest(BaseModel):
    topic: str

@app.get("/")
def home():
    return {"message": "Simple AI API running"}

@app.post("/study")
def study(request: TopicRequest):
    topic = request.topic
    return {
        "answer": f"{topic} is a concept used in technology to solve problems and improve efficiency."
    }
