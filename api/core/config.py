from os import environ
from logging import basicConfig, StreamHandler, FileHandler
from pathlib import Path

BASE_DIR = Path(__name__).resolve().parent.parent
LOGGING_FILENAME = BASE_DIR / "logs.log"
POSTGRES_CONNINFO = f"host=postgres port=5432 dbname=authorization_database password={environ.get("POSTGRES_PASSWORD")} user=authorization_api"
basicConfig(
    handlers={
        StreamHandler(),
        FileHandler(LOGGING_FILENAME, mode="w"),
    }
)
