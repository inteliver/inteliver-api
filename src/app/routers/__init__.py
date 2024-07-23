""" Routers Module.

    This module is responsible for registering different API routes.

"""

from fastapi import FastAPI

from app.users.router import router as users_router
from app.utils.i18n import _

from .version_router import router as version_router


def register_routers(app: FastAPI):
    app.include_router(users_router, prefix="/api/v1/users", tags=["Users"])

    app.include_router(version_router, prefix="/api/v1/inteliver-api", tags=["version"])

    # Root endpoint
    @app.get("/")
    async def root():
        return {"message": _("API is up and ok.")}
