from database.config import DATABASE_TYPE, DB_HOST, DB_NAME, DB_PASSWORD, DB_PORT, DB_USER
from peewee import PostgresqlDatabase

if DATABASE_TYPE == "postgres":
    import psycopg2
    from psycopg2.extensions import quote_ident


def get_postgres_database():
    return PostgresqlDatabase(DB_NAME, user=DB_USER, password=DB_PASSWORD, host=DB_HOST, port=DB_PORT)


def create_postgres_database():
    conn = psycopg2.connect(dbname="postgres", user=DB_USER, password=DB_PASSWORD, host=DB_HOST, port=DB_PORT)
    conn.autocommit = True
    cursor = conn.cursor()
    safe_db_name = quote_ident(DB_NAME, conn)
    cursor.execute(f"CREATE DATABASE {safe_db_name}")
    cursor.close()
    conn.close()
