import sqlite3
from pathlib import Path


def get_connection(database_filepath: Path) -> sqlite3.Connection | None:
    if Path.exists(database_filepath) and Path.is_file(database_filepath):
        return sqlite3.connect(database_filepath)

    return None
