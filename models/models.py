from pydantic import BaseModel

class PersonIn(BaseModel):
    """
    name(str): The name of the person.
    email(str): The email of the person.
    telephone(str): The telephone number of the person.
    id(int): The identification number of the person.
    """
    name: str
    email: str
    telephone: str
    id: int 

class PlaceIn(BaseModel):
    """
    name (str): The name of the place.
    ubication (str): The location of the place.
    type_place (str): The type of place.
    """
    name: str
    ubication: str
    type_place: str

class AutorizedPersonnelIn(BaseModel):
    """
    Attributes:
    name (str): The name of the authorized personnel.
    email (str): The email of the authorized personnel.
    telephone (str): The telephone number of the authorized personnel.
    id (int): The ID of the authorized personnel.
    rolname (str): The name of the role of the authorized personnel.
    roltype (str): The type of the role of the authorized personnel.
    rolcode (int): The code of the role of the authorized personnel.
    """
    name: str
    email: str
    telephone: str
    id: int
    rolname: str
    roltype: str
    rolcode: int

class EventIn(BaseModel):
    """
    Attributes:
    location (Place): The Place object where the event takes place.
    id (int): The ID of the event.
    timeIn (int): The time when the event starts.
    timeOut (int): The time when the event ends.
    date (str): The date when the event takes place.
    """
    place: PlaceIn
    id: int
    timeIn: int
    timeOut: int
    date: str

class VisitorIn(BaseModel):
    """
    responsible (AuthorizedPersonnel): The authorized personnel responsible for the visitor.
    event (Event): The event that the visitor is attending.
    name (str, optional): The name of the visitor. Defaults to 'name'.
    email (str, optional): The email of the visitor. Defaults to 'email'.
    telephone (str, optional): The telephone number of the visitor. Defaults to 'telephone'.
    id (int, optional): The ID of the visitor. Defaults to 0.
    """
    responsible: AutorizedPersonnelIn
    event: EventIn
    name: str 
    email: str
    telephone: str
    id: int

class PackageIn(BaseModel):
    """
    Attributes:
    subject (Visitor): The person who will carry the package.
    name (str): The name of the package.
    description (str): The description of the package (e.g. weight, size, etc.).
    code (int): The code of the package.
    """
    subject: VisitorIn
    name: str
    description: str
    code: int

class RegisterIn(BaseModel):
    """the registration class that will serve to register the entry of people is initialized"""
    subject: PersonIn
    zone: PlaceIn