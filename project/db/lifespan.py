from pathlib import Path

from aerich import Command

from tortoise import Tortoise, connections

from project.lib import settings


async def on_startup():
    """Connects to the database and creates the missing schemas on FastAPI startup."""

    async with Command(
        tortoise_config=settings.DATABASE, app="models", location="project/db/migrations"
    ) as command:
        parent_dir = Path(__file__).parent

        if not (parent_dir / "migrations").exists():
            await command.init_migrations(safe=True)

        await command.upgrade()

    await Tortoise.init(config=settings.CONFIG)


async def on_shutdown():
    """Closes the database connections on FastAPI shutdown."""

    await connections.close_all()
