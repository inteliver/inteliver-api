from pydantic import BaseModel, EmailStr
from typing import Optional


class UserCreate(BaseModel):
    name: str
    email_username: EmailStr
    password: str
    cloud_name: str
    endpoint: str
    storage_limit: int
    transaction_limit: int


class UserUpdate(BaseModel):
    name: Optional[str]
    cloud_name: Optional[str]
    endpoint: Optional[str]
    storage_limit: Optional[int]
    transaction_limit: Optional[int]


class UserOut(BaseModel):
    uid: str
    name: str
    email_username: str
    cloud_name: str
    endpoint: str
    storage_limit: int
    transaction_limit: int
    role: str

    class Config:
        orm_mode = True


class UserLogin(BaseModel):
    email_username: EmailStr
    password: str


class Token(BaseModel):
    access_token: str
    token_type: str
