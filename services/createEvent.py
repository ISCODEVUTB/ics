from models.models import EventIn
import json
from services.constans import dataPath

# Function to create a new event object in a JSON database
def create_event(event: EventIn):
    # Opening the JSON database and loading data
    with open(dataPath, "r") as f:
        data = json.load(f)

    # Adding the new event object to the 'events' list in the database
    data["events"].append(event.dict())

    # Saving the updated database to the JSON file
    with open(dataPath, "w") as f:
        json.dump(data, f)

    # Returning a success message
    return {"msg": "Event created succefully"}

