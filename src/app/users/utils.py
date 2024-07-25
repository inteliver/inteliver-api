from uuid import UUID

from passlib.context import CryptContext
from pydantic import EmailStr

from app.auth.schemas import TokenData, TokenScope

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def get_password_hash(password: str) -> str:
    return pwd_context.hash(password)


def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)


def verify_user_id_claim(user_id: UUID, token: TokenData) -> bool:
    if token.role == TokenScope.ADMIN:
        return True
    return user_id == token.sub


def verify_username_email_claim(username: EmailStr, token: TokenData) -> bool:
    if token.role == TokenScope.ADMIN:
        return True
    return username == token.username
