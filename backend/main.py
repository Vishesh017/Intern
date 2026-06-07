from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Hello Naveen Sir! The TechnoRise API is officially running."}