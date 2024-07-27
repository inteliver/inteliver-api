from datetime import datetime
from enum import Enum
from uuid import UUID

from pydantic import BaseModel, EmailStr


class UserRole(str, Enum):
    ADMIN = "admin"
    USER = "user"


class UserCreate(BaseModel):
    name: str
    email_username: EmailStr
    password: str


class UserUpdate(BaseModel):
    name: str | None = None


class UserPut(BaseModel):
    name: str


class UserOut(BaseModel):
    uid: UUID
    name: str
    email_username: str
    role: UserRole
    created_at: datetime | None
    updated_at: datetime | None

    class Config:
        from_attributes = True
        # This will use the string values of the enums
        use_enum_values = True


class UserLogin(BaseModel):
    email_username: EmailStr
    password: str
