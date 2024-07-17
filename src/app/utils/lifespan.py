from fastapi import FastAPI
from contextlib import asynccontextmanager
from loguru import logger
import gradio as gr

from app.interface import get_gr_interface
from app.config import settings


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
    return app


async def on_shutdown(app: FastAPI) -> None:
    """
    Executes shutdown tasks for the FastAPI application.

    Args:
        app (FastAPI): The FastAPI application instance.
    """
    logger.debug("Shutting down gracefully...")
    # Unregister any service that needs to be gracefully shut down
