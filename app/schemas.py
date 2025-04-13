from pydantic import BaseModel

class UserCreate(BaseModel):
    email: str
    pwd: str
    name: str
    role: str

class TokenData(BaseModel):
    email: str

class User(BaseModel):
    id: int
    email: str
    name: str
    role: str

    class Config:
        orm_mode = True
