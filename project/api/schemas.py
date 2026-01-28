from typing import Annotated

from pydantic import BaseModel, Field


NanoID = Annotated[
    str, Field(min_length=21, max_length=21, pattern="^[A-Za-z0-9_-]{21}$")
]
"""A nanoid identifier type for pydantic models.

Example:
```
from pydantic import BaseModel

from project.api.schemas import NanoID


class BookSchema(BaseModel):
    id: NanoID
    title: str
```
"""


class ErrorSchema(BaseModel):
    """A standard error response schema."""

    title: str
    message: str
