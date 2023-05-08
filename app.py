from fastapi import FastAPI
import json

from services.createPerson import create_person
from services.createPlace import create_place
from models.models import PersonIn
from models.models import PlaceIn
from services.constans import dataPath

app = FastAPI()

@app.get("/people")
async def get_people():
    with open(dataPath, "r") as f:
        data = json.load(f)

    return data['people']

@app.get("/places")
async def get_place():
    with open(dataPath, "r") as f:
        data = json.load(f)

    return data['places']

@app.post("/person")
async def create(person: PersonIn):
    createPerson = create_person(person)
    return {"Person": createPerson}


@app.post("/place")
async def create(place: PlaceIn):
    createPlace = create_place(place)
    return {"Place": createPlace}


