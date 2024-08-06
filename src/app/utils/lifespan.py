from contextlib import asynccontextmanager

from fastapi import FastAPI

from app.database.postgres import init_db
from app.utils.logger import logger


@asynccontextmanager
async def lifespan(app: FastAPI):
    await on_startup(app)
    yield
    await on_shutdown(app)


async def on_startup(app: FastAPI):
    """
    Executes startup tasks for the FastAPI application.

    Args:
        app (FastAPI): The FastAPI application instance.
    """
    logger.debug("Starting up the app...")
    # Register to services that needs to be created on startup
    await init_db()
    return app


async def on_shutdown(app: FastAPI) -> None:
    """
    Executes shutdown tasks for the FastAPI application.

    Args:
        app (FastAPI): The FastAPI application instance.
    """
    logger.debug("Shutting down gracefully...")
    # Unregister any service that needs to be gracefully shut down
