from datetime import datetime, timedelta, timezone
from typing import List, Optional

import jwt
from fastapi import Depends, HTTPException, Security, status
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError
from passlib.context import CryptContext
from pydantic import ValidationError
from sqlalchemy.ext.asyncio import AsyncSession

from app.auth.exceptions import ExpiredSignatureException, PyJWTException
from app.auth.schemas import TokenData
from app.config import settings
from app.users.crud import UserCRUD
from app.users.schemas import UserOut

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
oauth2_scheme = OAuth2PasswordBearer(tokenUrl=f"{settings.api_prefix}/auth/login")

SECRET_KEY = "your_secret_key"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30 * 24 * 60

oauth2_scheme = OAuth2PasswordBearer(tokenUrl=f"{settings.api_prefix}/auth/login")


class AuthService:
    oauth2_scheme = OAuth2PasswordBearer(tokenUrl=f"{settings.api_prefix}/auth/login")

    @staticmethod
    async def authenticate_user(
        db: AsyncSession, username: str, password: str
    ) -> Optional[UserOut]:
        """
        Authenticate a user by their username and password.

        Args:
            db (AsyncSession): The database session.
            username (str): The username of the user.
            password (str): The password of the user.

        Returns:
            Optional[UserOut]: The authenticated user or None if authentication fails.
        """
        user = await UserCRUD.get_user_by_email(db, username)
        if not user:
            return None
        if not pwd_context.verify(password, user.password):
            return None
        return UserOut.model_validate(user)

    @staticmethod
    def create_access_token(
        data: dict,
        expires_delta: Optional[timedelta] = timedelta(
            minutes=ACCESS_TOKEN_EXPIRE_MINUTES
        ),
    ):
        """
        Create a JWT token.

        Args:
            data (dict): Data to be encoded in the token.
            expires_delta (timedelta, optional): Expiration time for the token.
                Defaults to ACCESS_TOKEN_EXPIRE_MINUTES.

        Returns:
            str: The encoded JWT token.
        """
        to_encode = data.copy()
        expire = datetime.now(timezone.utc) + expires_delta
        to_encode.update({"exp": expire})
        encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
        return encoded_jwt

    @staticmethod
    def decode_access_token(token: str) -> TokenData:
        """
        Decode a JWT token.

        Args:
            token (str): The JWT token.

        Returns:
            TokenData: The decoded token data.

        Raises:
            HTTPException: If the token is expired or invalid.
        """
        try:
            payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
            token_data = TokenData(
                sub=payload.get("sub"),
                role=payload.get("role"),
                username=payload.get("username"),
            )
            return token_data

        except jwt.ExpiredSignatureError:
            raise ExpiredSignatureException
        except jwt.PyJWTError:
            raise PyJWTException
        except ValidationError:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Token fields validation failed",
            )

    @classmethod
    def get_current_user(cls, token: str = Depends(oauth2_scheme)) -> TokenData:
        return AuthService.decode_access_token(token)

    @classmethod
    def has_role(cls, role: str):
        """
        Role checker to verify the user's role.

        Args:
            role (str): The role to check.

        Returns:
            callable: A dependency that checks the user's role.

        Raises:
            HTTPException: If the user does not have the required role.
        """

        def role_checker(
            current_user: TokenData = Security(cls.get_current_user),
        ):
            if current_user.role == "admin":
                return current_user
            if not role == current_user.role:
                raise HTTPException(
                    status_code=status.HTTP_403_FORBIDDEN,
                    detail="Not enough permissions",
                )
            return current_user

        return role_checker
