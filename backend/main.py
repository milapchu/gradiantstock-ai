from fastapi import FastAPI
import os

app = FastAPI()

@app.get("/")
def hello():
    return {"status": "GradiantStock Backend Live", "db": "Connected" if os.getenv("DATABASE_URL") else "Missing URL"}
