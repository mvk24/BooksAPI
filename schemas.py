# Pydantic models for response/request
from pydantic import BaseModel, ConfigDict

class BookBase(BaseModel):
    title: str
    author: str
    genere: str
    yop: int
    description: str
    price: float


class BookCreate(BookBase):
    pass

class BookOut(BookBase):
    id: int

    model_config = {"from_attributes" : True }  #Enables ORM compatiblity
