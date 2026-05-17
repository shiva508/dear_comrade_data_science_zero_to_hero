from pydantic import BaseModel, Field
from typing import Literal


class MedicalTest(BaseModel):
    name: str= Field(description="Medical test name"),
    description: str= Field(description="Medical test description")

class User(BaseModel):
    name: str= Field(description="User's name"),
    email: str= Field(description="User's email"),
    phone: str= Field(description="User's phone number"),
    address: str= Field(description="User's address"),
    id: int= Field(description="User's id"),