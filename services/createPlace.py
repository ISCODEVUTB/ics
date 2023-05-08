from models.models import PlaceIn
import json
from services.constans import dataPath

# Function to create a new place object in a JSON database
def create_place(place: PlaceIn):
    # Opening the JSON database and loading data
    with open(dataPath, "r") as f:
        data = json.load(f)

    # Adding the new place object to the 'places' list in the database
    data["places"].append(place.dict())

    # Saving the updated database to the JSON file
    with open(dataPath, "w") as f:
        json.dump(data, f)

    # Returning a success message
    return {"msg": "Person created succefully"}