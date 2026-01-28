import os

from dotenv import load_dotenv


load_dotenv()


DEBUG = os.getenv("DEBUG", "False").lower() in ("true", "1", "t")


DATABASE = {
    "connections": {"default": os.getenv("DATABASE_URL", "sqlite://db.sqlite3")},
    "apps": {
        "models": {
            "models": [
                "project.db.models.example",
                "aerich.models",  # Keep this one for migrations.
            ],
            "default_connection": "default",
        }
    },
    "use_tz": True,
    "timezone": "UTC",
}
