from typing import List
from fastapi import FastAPI
from fastapi.responses import FileResponse
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

from dotenv import load_dotenv

import os
import json
import sys

app = FastAPI()

origins = [
    "http://localhost",
    "http://localhost:8080",
    "http://0.0.0.0",
    "http://0.0.0.0:8080",
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

env = load_dotenv()

DIRECTORY_PATH = os.getenv("DIRECTORY_PATH")
DIRECTORY_IMAGE = os.path.join(DIRECTORY_PATH, "image")

SESSION = "session"
JSON_PATH = os.path.join(SESSION, "info.json")
json_info = None


def positive_hash(string):
    return (hash(string) + sys.maxsize + 1) % sys.maxsize


def save_json():
    with open(JSON_PATH, "w") as f:
        json.dump(json_info, f)


def new_json():
    global json_info
    files = os.listdir(DIRECTORY_IMAGE)
    with open(JSON_PATH, "w") as f:
        json_info = dict()
        json_info["images"] = []
        for file in files:
            info = dict()
            info["name"] = file
            info["hash"] = positive_hash(file)
            info["enabled"] = True
            json_info["images"].append(info)
        json_info["music"] = dict()
        json_info["music"]["enabled"] = False
        json_info["music"]["volume"] = 0.5
        json_info["music"]["bpm"] = None


@app.get('/')
async def main_root():

    global json_info
    if not os.path.exists(SESSION):
        os.makedirs(SESSION)

    if not os.path.exists(JSON_PATH):
        new_json()
    else:
        with open(JSON_PATH, "r") as f:
            json_info = json.load(f)

    return json_info


@app.get("/images/{filename}")
async def get_image(filename):
    return FileResponse(os.path.join(DIRECTORY_IMAGE, filename))


@app.get("/images/{filename}/info")
async def get_image(filename):
    images = json_info["images"]
    image = next(filter(lambda x: x["name"] == filename, images), None)
    return image


@app.get("/images/{filename}/switch")
async def get_image(filename):
    global json_info
    images = json_info["images"]
    image = next(filter(lambda x: x["name"] == filename, images), None)
    index = images.index(image)

    image["enabled"] = not image["enabled"]
    images[index] = image

    json_info["images"] = images

    save_json()

    return image["enabled"]


@app.get("/reload")
async def reload():
    new_json()
    save_json()
    return json_info


class Reorder(BaseModel):
    name: str


@app.post("/reorder")
async def reorder(data: List[Reorder]):
    global json_info
    images = json_info["images"]
    new_images = []
    for datum in data:
        image = next(filter(lambda x: x["name"] == datum.name, images), None)
        new_images.append(image)
    json_info["images"] = new_images

    save_json()
    return json_info
