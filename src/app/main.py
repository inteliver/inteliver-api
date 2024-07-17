"""
    Main script of AI Service Template.

    This script setups the API server using FastAPI.

"""

from fastapi import FastAPI

from app.routers import register_routers
from app.utils.lifespan import lifespan
from app.version import __version__
from app.config import settings
from app.utils.middleware import LanguageMiddleware
from app.utils.lifespan import mount_gradio_ui


service_description = """
# AI Service Template 🚀
Welcome to the AI Service Template repository! 🤖 This template is designed for building AI services
using FastAPI as the REST API server, with Docker and docker-compose for containerization. 🐳

### GET `/version`

This endpoints return the version of the code.
"""

service_title = "FastAPI AI Service Template"
service_summary = "This template is designed for building AI services using FastAPI as the REST API server"


app = FastAPI(
    lifespan=lifespan,
    title=service_title,
    summary=service_summary,
    description=service_description,
    version=__version__,
    docs_url=settings.openapi_docs_url,
    openapi_url=settings.openapi_json_url,
    # root_path=os.environ.get("FASTAPI_ROOT_PATH", "/api/v1"),
)


register_routers(app)
app.add_middleware(LanguageMiddleware)
app = mount_gradio_ui(app)


def run_service(host: str = settings.app_api_host, port: int = settings.app_api_port):
    import uvicorn

    uvicorn.run(app, host=host, port=port)


if __name__ == "__main__":
    run_service()
