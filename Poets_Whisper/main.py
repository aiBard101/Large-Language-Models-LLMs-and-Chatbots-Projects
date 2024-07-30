import os
from app import GoogleAI

os.environ["GOOGLE_API_KEY"] = ""
api_key = os.environ.get("GOOGLE_API_KEY")

ai =  GoogleAI(api_key)

from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse, FileResponse
from fastapi.staticfiles import StaticFiles
import time
import asyncio

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/", response_class=HTMLResponse)
async def read_index():
    with open("index.html") as f:
        return HTMLResponse(content=f.read(), status_code=200)

@app.post("/generate-poem/")
async def generate_poem(request: Request):
    data = await request.json()
    user_input = data.get("userInput")

    # await asyncio.sleep(1)

    title, poem = ai.poem(user_input)
    loading_message = ai.load_message(user_input)
    
    # title = "Poem"
    # poem = "Little starr"
    # loading_message = "Please wait"
    return {"title": title, "poem": poem, "loadingMessage": loading_message}
