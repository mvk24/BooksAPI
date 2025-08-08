from pydantic import BaseModel, EmailStr, Field, field_validator, ConfigDict
from typing import Optional

class UserBase(BaseModel):
    username: str = Field(..., min_length = 3, max_length = 20, example = "User Name")
    email: EmailStr = Field(..., example = "user@gmail.com")
    role: Optional[str] = "user"
    

    @field_validator('username', mode = 'before')
    @classmethod
    def reject_defalut_strings(cls, value):
        if value.strip().lower() in ["", "username", "string", "ok", "na", "none", "n/a"]:
                raise ValueError("Fields cannot be default placeholder")
        return value

class UserCreate(UserBase):
    password: str = Field(..., min_length = 6, example = "strongpassword")

    @field_validator('password', mode = 'before')
    @classmethod
    def reject_defalut_strings(cls, value):
        if value.strip().lower() in ["","strongpassword", "string", "ok", "na", "none", "n/a"]:
                raise ValueError("Fields cannot be default placeholder")
        return value

class UserUpdate(UserBase):
     password: str = None


class SelfRegister(BaseModel):
    username: str = Field(..., min_length = 3, max_length = 20, example = "User Name")
    email: EmailStr = Field(..., example = "user@gmail.com")
    password: str = Field(..., min_length = 6, example = "strongpassword")
     

class UserOut(BaseModel):
    id: int
    username: str
    email: EmailStr
    role: str

    class Config:
        #  model_config = ConfigDict(orm_mode = True)
        from_attributes = True
    