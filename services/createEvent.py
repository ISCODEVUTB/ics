from models.models import EventIn
import json
import string
import random
from services.constans import dataPath

# Function to create a new event object in a JSON database
def create_event(event: EventIn):
    # Opening the JSON database and loading data
    with open(dataPath, "r") as f:
        data = json.load(f)

    # Adding the new event object to the 'events' list in the database
    data["events"].append(event.dict())

    """number_of_strings = 5
    length_of_string = 8
    for x in range(number_of_strings):
        credential= ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(length_of_string))

        
    event_name = event.dict()["name"]
    credential_entry = {"name": event_name, "credential": credential}
    data["credentials"].append(credential_entry)"""

    # Saving the updated database to the JSON file
    with open(dataPath, "w") as f:
        json.dump(data, f)

    # Returning a success message
    return {"msg": "Event created succefully"}

