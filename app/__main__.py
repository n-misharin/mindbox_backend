from fastapi import FastAPI

from app.config.utils import get_settings
from app.endpoints import list_of_routes


def bind_routes(application: FastAPI, settings) -> None:
    for route in list_of_routes:
        application.include_router(route, prefix=settings.PATH_PREFIX)


def get_app() -> FastAPI:
    application = FastAPI(
        title="Market",
        docs_url="/swagger",
        openapi_url="openapi",
    )
    settings = get_settings()
    bind_routes(application, settings)

    return application
