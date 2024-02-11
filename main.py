from fastapi import FastAPI 
from typing import Optional
import uvicorn

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}


