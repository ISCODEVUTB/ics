from models.models import PersonIn
import json
from services.constans import dataPath

def create_person(person: PersonIn):
    with open(dataPath, "r") as f:
        data = json.load(f)

    data["people"].append(person.dict())

    with open(dataPath, "w") as f:
        json.dump(data, f)

    return {"msg": "Person created succefully"} 