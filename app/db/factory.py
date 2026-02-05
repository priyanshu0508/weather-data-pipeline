from config import DB_TYPE
from db.sqlite_db import SQLiteClient
from db.postgres_db import PostgresClient

def get_db_client():
    if DB_TYPE == "postgres":
        return PostgresClient()
    return SQLiteClient()
