from typing import Optional
from uuid import UUID

from pydantic import BaseModel, EmailStr


class UserCreate(BaseModel):
    name: str
    email_username: EmailStr
    password: str
    cloud_name: str
    endpoint: str
    storage_limit: int
    transaction_limit: int


class UserUpdate(BaseModel):
    name: str | None = None
    cloud_name: str | None = None
    endpoint: str | None = None
    storage_limit: int | None = None
    transaction_limit: int | None = None


class UserPut(BaseModel):
    name: str
    cloud_name: str
    endpoint: str
    storage_limit: int
    transaction_limit: int


class UserOut(BaseModel):
    uid: UUID
    name: str
    email_username: str
    cloud_name: str
    endpoint: str
    storage_limit: int
    transaction_limit: int
    role: str

    class Config:
        from_attributes = True


class UserLogin(BaseModel):
    email_username: EmailStr
    password: str
