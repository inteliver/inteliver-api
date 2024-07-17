""" Routers Module.

    This module is responsible for registering different API routes.

"""

from fastapi import FastAPI
from .version_router import router as version_router
from app.utils.i18n import _


def register_routers(app: FastAPI):
    app.include_router(
        version_router, prefix="/api/v1/inteliver-api", tags=["version"]
    )

    # Root endpoint
    @app.get("/")
    async def root():
        return {"message": _("API is up and ok.")}
