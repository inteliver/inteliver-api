from typing import List, Optional
from uuid import UUID

from pydantic import BaseModel


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    sub: UUID
    role: str
    username: str
    # roles: List[str] = []


class LoginForm(BaseModel):
    username: str
    password: str


class OTPForm(BaseModel):
    username: str
    otp: str
