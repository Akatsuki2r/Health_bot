from fastapi import FastAPI
from contextlib import asynccontextmanager

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


