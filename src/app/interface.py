import os

import asyncio
import gradio as gr


service_description = """
# AI Service Template

Welcome to the AI Service Template repository! This template is designed for building AI services
using FastAPI as the REST API server, with Docker and docker-compose for containerization.

## Main Folders

- **app:** Main application code resides here.
  - **app/assets:** Houses assets and AI models.
  - **app/controllers:** Contains the controllers and logic code for the server.
  - **app/errors:** Holds error response definitions.
  - **app/routers:** Routers for defining API paths.
  - **app/schemas:** Pydantic schemas for the API.
  - **app/utils:** Any additional utility functions can be found here.
  - **app/main.py:** The main FastAPI file.

- **docs:** Auto-generated code documentation. Do not modify this directory; it's generated using `make docs`.

- **tests:** Primary folder for unit tests and integration tests.

"""


def greet(name, intensity):
    return "Hello " * intensity + name + "!"


def get_gr_interface():
    return gr.Interface(
        fn=greet,
        inputs=["text", "slider"],
        outputs=["text"],
        examples=[["Hello", 5], ["Hi", 2]],
        title="AI Service Template",
        description=service_description,
        allow_flagging="never",
        flagging_dir=os.path.abspath("app/assets/flagged"),
        concurrency_limit=5,
    )


if __name__ == "__main__":
    asyncio.run(get_gr_interface().launch())
