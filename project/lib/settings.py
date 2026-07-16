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
            ],
            "default_connection": "default",
            "migrations": "project.db.migrations",
        }
    },
    "use_tz": True,
    "timezone": "UTC",
}
