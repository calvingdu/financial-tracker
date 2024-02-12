from fastapi import FastAPI 
from googleapiclient.discovery import build
from typing import Optional
import credential_handler
import uvicorn
import get

app = FastAPI()

credential_handler.get_creds()

@app.get("/grab")
async def grab():
    return get.get_values()





