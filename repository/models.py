from pydantic import BaseModel
from sqlalchemy import  Column, Integer, String, Float

from .database import Base

class Address(Base):
    __tablename__ = "addresses"

    id = Column(Integer, primary_key=True, index=True)
    street = Column(String, index=True)
    city = Column(String, index=True)
    latitude = Column(Float)
    longitude = Column(Float)

