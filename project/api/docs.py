import os

from enum import Enum

from dataclasses import dataclass

from fastapi import FastAPI
from fastapi.routing import APIRoute


@dataclass
class OpenAPI:
    summary: str | None
    description: str | None
    tags: list["OpenAPITag"]

    @classmethod
    def load(cls, base_path: str) -> "OpenAPI":
        """Loads the OpenAPI documentation strings from a path.

        Inside that path:
            _Summary.md -> The OpenAPI summary.
            _Description.md -> The OpenAPI description.
            *.md -> Tags, the file name without the prefix is the tag name and the file
                contents is the description.

        Args:
            base_path (str): The path to the directory where the files are.

        Returns:
            OpenAPI: The initialized OpenAPI object.
        """

        summary = None
        description = None
        tags = []

        dirs = os.listdir(base_path)
        dirs.sort()

        for doc_file in dirs:
            if not doc_file.endswith(".md"):
                continue

            with open(f"{base_path}/{doc_file}", "r", encoding="utf-8") as f:
                content = f.read()

                name = doc_file.split(".")[0]

                if name == "_Summary":
                    summary = content

                elif name == "_Description":
                    description = content

                else:
                    tags.append(OpenAPITag(name=name, description=content))

        return cls(summary=summary, description=description, tags=tags)


@dataclass
class OpenAPITag:
    name: str
    description: str


def load(base_path: str) -> OpenAPI:
    """Loads the OpenAPI documentation strings from a path.

    Inside that path:
        _Summary.md -> The OpenAPI summary.
        _Description.md -> The OpenAPI description.
        *.md -> Tags, the file name without the prefix is the tag name and the file
            contents is the description.

    Args:
        base_path (str): The path to the directory where the files are.

    Returns:
        OpenAPI: The initialized OpenAPI object.
    """

    return OpenAPI.load(base_path)


def load_onto_fastapi(
    base_path: str,
    app: FastAPI,
    *,
    only_tags: list[str | Enum] = None,
    only_used_tags: bool = True,
) -> None:
    """Loads the OpenAPI summaries and descriptions and loads them onto a `FastAPI`
    application.

    Read `load()`'s documentation for information about structure.

    Args:
        base_path (str): The path to the directory where the files are.
        app (FastAPI): The app to load the docs onto.
        only_tags (list[str | Enum], optional): A list of tags to load. If not
            provided, all tags will be loaded. Defaults to None.
        only_used_tags (bool, optional): If True, only tags that are used in the
            app's routes will be loaded. Defaults to True.
    """

    openapi = OpenAPI.load(base_path)

    if only_tags is not None and only_used_tags:
        raise ValueError("Cannot use both `only_tags` and `only_used_tags`.")

    if only_used_tags:
        used_tags = set()

        for route in app.routes:
            if isinstance(route, APIRoute):
                for tag in route.tags:
                    used_tags.add(tag)

        openapi.tags = [tag for tag in openapi.tags if tag.name in used_tags]

    elif only_tags is not None:
        only_tags = [tag.value if isinstance(tag, Enum) else tag for tag in only_tags]
        openapi.tags = [tag for tag in openapi.tags if tag.name in only_tags]

    app.summary = openapi.summary
    app.description = openapi.description
    app.openapi_tags = []

    for tag in openapi.tags:
        app.openapi_tags.append(
            {
                "name": tag.name,
                "description": tag.description,
            }
        )
