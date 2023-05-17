from models.models import PersonIn
import json
from services.constans import dataPath

# Function to create a new person object in the JSON database
def create_person(person: PersonIn):
    # Opening the JSON database and loading data
    with open(dataPath, "r") as f:
        data = json.load(f)

    # Adding the new person object to the 'people' list in the database
    data["people"].append(person.dict())

    # Saving the updated database to the JSON file
    with open(dataPath, "w") as f:
        json.dump(data, f)

    # Returning a success message
    return {"msg": "Person created succefully"} 