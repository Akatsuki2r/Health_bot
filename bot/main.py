from fastapi import FastAPI
from contextlib import asynccontextmanager
import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from models.schemas import JournalEntry

bot = FastAPI()

@asynccontextmanager
async def lifespan(bot: FastAPI):
    print("Starting...")
    # connect to things
    yield
    print("Shutting down...")
    # cleanup or shutdown

bot = FastAPI(lifespan=lifespan)

@bot.get("/")
async def read():
    return {"message": "Health Bot is live"}

@bot.post("/journal")
async def write_journal(entry: JournalEntry):
    #Analyze journal text through the emotion.py
    analysis = detect_emotions_and_symp
    


