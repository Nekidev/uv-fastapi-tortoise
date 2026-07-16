from fastapi import FastAPI
from fastapi.responses import ORJSONResponse

from project.lib import settings
from project.api.lifespan import lifespan
from project.api.v1 import app as app_v1
from project.api.v1.errors import NotFoundError


app = FastAPI(
    debug=settings.DEBUG,
    docs_url=None,
    redoc_url=None,
    lifespan=lifespan,
    default_response_class=ORJSONResponse,
)


app.add_exception_handler(404, NotFoundError.handler)


app.mount("/v1", app_v1, name="v1")
