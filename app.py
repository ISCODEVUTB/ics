from fastapi import FastAPI
import json

# Importing required services and models
from services.createPerson import create_person
from services.createPlace import create_place
from models.models import PersonIn
from models.models import PlaceIn
from services.constans import dataPath

# Initializing the FastAPI app
app = FastAPI()

# A GET endpoint to retrieve all people data from a database
@app.get("/people")
async def get_people():
    with open(dataPath, "r") as f:
        data = json.load(f)

    return data['people']

# A GET endpoint to retrieve all places data from a database
@app.get("/places")
async def get_place():
    with open(dataPath, "r") as f:
        data = json.load(f)

    return data['places']

# A POST endpoint to create a new person object in the database
@app.post("/person")
async def create(person: PersonIn):
    createPerson = create_person(person)
    return {"Person": createPerson}

# A POST endpoint to create a new place object in the database
@app.post("/place")
async def create(place: PlaceIn):
    createPlace = create_place(place)
    return {"Place": createPlace}


