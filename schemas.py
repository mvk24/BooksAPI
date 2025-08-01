# Pydantic models for response/request
from pydantic import BaseModel, Field, field_validator
from typing import Optional

class BookBase(BaseModel):
    title: str = Field(..., min_length = 3)
    author: str = Field(..., min_length= 3)
    genre: Optional[str] = None
    yop: Optional[int] = None
    description: Optional[str] = None
    price: Optional[float] = None


    @field_validator('title', 'author', 'genre', 'description')
    @classmethod
    def reject_defalut_strings(cls, value):
            if value.strip().lower() in ["", "string", "ok", "na", "none", "n/a"]:
                raise ValueError("Fields cannot be default placeholder")
            return value


class BookCreate(BookBase):
    pass

class BookUpdate(BookBase):
    pass

class BookOut(BookBase):
    id: int

    class Config :
         from_attributes = True  
