from fastapi import FastAPI
from fastapi.responses import ORJSONResponse

from project.lib import settings
from project.api import docs
from project.api.errors import BaseError, NotFoundError
from project.api.lifespan import lifespan
from project.api.example.router import router as example_router


app = FastAPI(
    debug=settings.DEBUG,
    title="Project API",
    description=docs.OPENAPI_DESCRIPTION,
    version="1.0.0",
    docs_url=None,
    redoc_url="/docs",
    lifespan=lifespan,
    openapi_tags=docs.OPENAPI_TAGS,
    default_response_class=ORJSONResponse,
)


app.include_router(example_router)

app.add_exception_handler(BaseError, BaseError.handler)
app.add_exception_handler(404, NotFoundError.handler)
