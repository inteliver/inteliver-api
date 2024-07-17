import socket
import os
import py_eureka_client.eureka_client as eureka_client
from loguru import logger

from app.config import settings


EUREKA_URL = os.environ.get("EUREKA_URL")


async def register_service():
    if settings.eureka_discovery_enable:
        try:
            my_ip_address = socket.gethostbyname(socket.gethostname())
            await eureka_client.init_async(
                eureka_server=settings.eureka_discovery_url,
                app_name=settings.app_name,
                instance_port=settings.app_api_port,
                instance_ip=my_ip_address,
                instance_host=my_ip_address,
            )
        except Exception as e:
            logger.error(f"Error Occured in Registering: {e}")
    else:
        logger.debug(
            "CONFIG_EUREKA_DISCOVERY_URL env variable not set. Not registering to the discovery service."
        )


async def unregister_service():
    if settings.eureka_discovery_enable:
        try:
            logger.debug("Unregistering from the discovery service.")
            eureka_client.stop_async()
        except Exception as e:
            logger.error(f"Error Occured in Unregistering: {e}")
