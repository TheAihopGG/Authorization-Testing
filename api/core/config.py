from logging import basicConfig, StreamHandler, FileHandler
from pathlib import Path

BASE_DIR = Path(__name__).resolve().parent.parent
LOGGING_FILENAME = BASE_DIR / "logs.log"
basicConfig(
    handlers={
        StreamHandler(),
        FileHandler(LOGGING_FILENAME, mode="w"),
    }
)
