from fastapi import FastAPI
from enum import Enum
from fastapi import FastAPI
from pydantic import BaseModel
from typing import List



app = FastAPI()
@app.get("/home")
async def home():
    return "welcome home:"
