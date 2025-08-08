# Pydantic models for response/request
from pydantic import BaseModel, Field, field_validator, ConfigDict
from typing import Optional
from schemas.user_schema import UserOut

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
            if value is None:
                 return value
            if value.strip().lower() in ["", "string", "ok", "na", "none", "n/a"]:
                raise ValueError("Fields cannot be default placeholder")
            return value


class BookCreate(BookBase):
    pass

class BookUpdate(BookBase):
    pass

class BookOut(BookBase):
    id: int
    owner_id: Optional[int]
    owner: Optional[UserOut] = None

    class Config :
        #  model_config = ConfigDict(orm_mode = True)
         from_attributes = True  
