from fastapi import FastAPI

from contextlib import asynccontextmanager

from project.db.lifespan import on_startup, on_shutdown


@asynccontextmanager
async def lifespan(app: FastAPI):
    await on_startup()

    yield

    await on_shutdown()
