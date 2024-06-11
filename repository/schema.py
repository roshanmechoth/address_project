
from pydantic import BaseModel



class AddressData(BaseModel):
    street: str
    city: str
    latitude: float
    longitude: float
