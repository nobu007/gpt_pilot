from database.config import DB_NAME
from peewee import SqliteDatabase


def get_sqlite_database():
    return SqliteDatabase(DB_NAME)
