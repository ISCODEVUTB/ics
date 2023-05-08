from models.models import PlaceIn
import json
from services.constans import dataPath

def create_place(place: PlaceIn):
    with open(dataPath, "r") as f:
        data = json.load(f)

    data["places"].append(place.dict())

    with open(dataPath, "w") as f:
        json.dump(data, f)

    return {"msg": "Person created succefully"}