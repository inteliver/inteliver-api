from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from sqlalchemy.ext.asyncio import AsyncSession

from app.auth.exceptions import AuthenticationFailedException
from app.auth.schemas import LoginForm, Token
from app.auth.service import AuthService
from app.config import settings
from app.database.dependencies import get_db

router = APIRouter()


@router.post("/login", response_model=Token)
async def login(
    form_data: Annotated[OAuth2PasswordRequestForm, Depends()],
    db: AsyncSession = Depends(get_db),
):
    """
    Authenticate a user and return a JWT token.

    This endpoint takes a username and password from the `LoginForm` and
    authenticates the user. If the credentials are correct, it returns
    a JWT token.

    Args:
        form_data (LoginForm): Form data containing username and password.
        db (AsyncSession): Database session dependency.

    Returns:
        Token: JWT token with access token and token type.

    Raises:
        HTTPException: If authentication fails, raises a 401 unauthorized status code
            with a message indicating incorrect username or password.
    """
    user = await AuthService.authenticate_user(
        db, form_data.username, form_data.password
    )
    if not user:
        raise AuthenticationFailedException
    access_token = AuthService.create_access_token(
        data={"sub": str(user.uid), "username": user.email_username, "role": user.role}
    )
    return Token(access_token=access_token, token_type="bearer")


@router.post("/logout")
async def logout(token: str = Depends(AuthService.oauth2_scheme)):
    """
    Log out the user by invalidating their token.

    This endpoint takes the user's JWT token and invalidates it, effectively
    logging out the user. The actual invalidation logic can vary based on the
    implementation and requirements, such as:

    - Adding the token to a blacklist.
    - Maintaining a session store and marking the session as invalid.
    - Setting token expiration to the past.

    Args:
        token (str): The JWT token provided by the user.

    Returns:
        dict: A message indicating successful logout.
    """

    # Implement token invalidation logic
    # For example, add the token to a blacklist or invalidate
    # the session in the database
    return {"msg": "Successfully logged out"}


@router.post("/refresh", response_model=Token)
async def refresh_token(token: str = Depends(AuthService.oauth2_scheme)):
    """
    Refresh the user's JWT token.

    This endpoint takes the user's JWT token, validates it, and issues a new
    token with updated expiration. It allows users to stay authenticated without
    having to log in again frequently.

    Args:
        token (str): The JWT token provided by the user.

    Returns:
        dict: A new JWT token with updated expiration and the token type.
    """
    token_data = AuthService.decode_access_token(token)
    new_token = AuthService.create_access_token(
        data={
            "sub": str(token_data.sub),
            "username": token_data.username,
            "role": token_data.role,
        }
    )
    return Token(access_token=new_token, token_type="bearer")
