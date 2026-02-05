from db.base import DatabaseClient
import psycopg2
from config import POSTGRES_CONFIG

class PostgresClient(DatabaseClient):

    def insert_weather(self, data):
        raise NotImplementedError("Postgres insert not enabled yet")

    def get_last_ingestion_time(self):
        raise NotImplementedError("Postgres query not enabled yet")
