from datetime import datetime, timedelta, timezone
from typing import Optional
from uuid import UUID

import jwt
from fastapi import Depends, HTTPException, Security, status
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError
from loguru import logger
from passlib.context import CryptContext
from pydantic import EmailStr, ValidationError
from sqlalchemy.ext.asyncio import AsyncSession

from app.auth.exceptions import (
    AuthenticationFailedException,
    ExpiredSignatureException,
    NotEnoughPermissionException,
    PyJWTException,
)
from app.auth.schemas import PasswordChange, PasswordResetToken, TokenData
from app.auth.utils import get_password_hash, verify_password
from app.config import settings
from app.users.crud import UserCRUD
from app.users.exceptions import UserNotFoundException
from app.users.models import User
from app.users.schemas import UserOut, UserRole

SECRET_KEY = "your_secret_key"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30 * 24 * 60  # 1 month
RESET_PASSWORD_EXPIRE_MINUTES = 60  # 1 hour


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
        if not verify_password(password, user.password):
            return None
        return UserOut.model_validate(user)

    @staticmethod
    async def change_password(
        db: AsyncSession, user_id: UUID, password_change: PasswordChange
    ) -> None:
        """
        Change the password for a user.

        Args:
            db (AsyncSession): The database session.
            user_id (UUID): The ID of the user.
            new_password (str): The new password.

        Returns:
            None
        """
        user = await UserCRUD.get_user_by_id(db, user_id)
        if not user:
            raise UserNotFoundException(f"User with id {user_id} not found")

        if not verify_password(password_change.current_password, user.password):
            raise AuthenticationFailedException

        await UserCRUD.update_user_password(
            db, user, get_password_hash(password_change.new_password)
        )

    @staticmethod
    async def send_password_reset_email(db: AsyncSession, email: str) -> None:
        """
        Send a password reset email with a token.

        Args:
            db (AsyncSession): The database session.
            email (str): The email address of the user.

        Returns:
            None

        Raises:
            HTTPException: If the user is not found.
        """
        user = await UserCRUD.get_user_by_email(db, email)
        if not user:
            raise UserNotFoundException(f"User with email {email} not found")

        reset_token = AuthService.create_password_reset_token(user)
        # Here you would implement the actual email sending logic.
        # For example, using a third-party email service like SendGrid or SMTP.
        # send_email(user.email, "Password Reset", f"Your reset token: {reset_token}")

        logger.debug(
            f"Password reset token created for user {user.email_username}: {reset_token}"
        )

    @staticmethod
    def create_password_reset_token(user: User) -> str:
        """
        Create a password reset token.

        Args:
            user (User): The user object.

        Returns:
            str: The encoded JWT token.
        """
        expire = datetime.now(timezone.utc) + timedelta(
            minutes=RESET_PASSWORD_EXPIRE_MINUTES
        )
        to_encode = {"sub": str(user.uid), "exp": expire}
        return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

    @staticmethod
    async def reset_password(db: AsyncSession, token: str, new_password: str) -> None:
        """
        Reset the user's password using a reset token.

        Args:
            db (AsyncSession): The database session.
            token (str): The password reset token.
            new_password (str): The new password.

        Returns:
            None

        Raises:
            HTTPException: If the token is invalid or expired.
        """
        try:
            payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
            token_data = PasswordResetToken(
                sub=payload.get("sub"),
                exp=payload.get("exp"),
            )
        except jwt.ExpiredSignatureError:
            raise ExpiredSignatureException
        except jwt.PyJWTError:
            raise PyJWTException
        except ValidationError:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Token fields validation failed",
            )

        user = await UserCRUD.get_user_by_id(db, token_data.sub)
        if not user:
            raise UserNotFoundException(f"User with id {token_data.sub} not found")

        await UserCRUD.update_user_password(db, user, get_password_hash(new_password))

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
    def has_role(cls, role: UserRole):
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
            if current_user.role == UserRole.ADMIN:
                return current_user
            if not role == current_user.role:
                raise NotEnoughPermissionException
            return current_user

        return role_checker
