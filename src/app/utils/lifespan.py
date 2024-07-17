from fastapi import FastAPI
from contextlib import asynccontextmanager
from loguru import logger
import gradio as gr

from app.interface import get_gr_interface
from app.utils.eureka import register_service, unregister_service
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
    # Mount Gradio dev UI if configured
    # Not working in this fashion
    # await mount_gradio_ui(app)
    # Register to service discovery if applicable
    await register_service()
    return app


async def on_shutdown(app: FastAPI) -> None:
    """
    Executes shutdown tasks for the FastAPI application.

    Args:
        app (FastAPI): The FastAPI application instance.
    """
    logger.debug("Shutting down gracefully...")
    # Unregister from service discovery if applicable
    await unregister_service()


def mount_gradio_ui(app: FastAPI) -> FastAPI:
    """
    Mounts the Gradio UI interface if enabled.

    Args:
        app (FastAPI): The FastAPI application instance.
    """
    if settings.gradio_interface_enable:
        logger.debug("Gradio UI is enabled. Mounting Gradio interface app...")
        app = gr.mount_gradio_app(
            app,
            get_gr_interface(),
            path=settings.gradio_interface_url,
        )
        return app
    return app
