from fastapi import APIRouter

from project.api.example.schemas import MessageSchema


router = APIRouter(tags=["Example"])


@router.get("/hello")
async def hello_world() -> MessageSchema:
    """An example API endpoint that returns a hello world message."""

    return MessageSchema(message="Hello, World!")
