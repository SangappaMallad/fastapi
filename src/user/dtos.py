# dtos: data transfer objects

from pydantic import BaseModel


class UserSchema(BaseModel):
    name : str
    userName : str
    password : str
    email : str

class UserResponseSchema(BaseModel):
    id: int
    name : str
    userName : str
    email : str

class LoginSchema(BaseModel):
    userName : str
    password : str
