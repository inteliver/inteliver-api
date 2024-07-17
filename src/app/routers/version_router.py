from fastapi import APIRouter, status

from app.schemas.version import Version
from app.version import __version__


router = APIRouter()


@router.get("/version", response_model=Version, status_code=status.HTTP_200_OK)
async def get_app_version():
    """
    Retrieve the application version.

    Returns:
        Version: The pydantic model for app version.
    """
    return Version(version=__version__)
