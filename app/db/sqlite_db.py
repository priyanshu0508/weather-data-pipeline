from db.base import DatabaseClient
from database import get_connection

class SQLiteClient(DatabaseClient):

    def insert_weather(self, data):
        conn = get_connection()
        cur = conn.cursor()

        cur.execute("""
        INSERT INTO weather_data
        (city_id, temperature, humidity, pressure, description, timestamp)
        VALUES (?, ?, ?, ?, ?, ?)
        """, data)

        conn.commit()
        conn.close()

    def get_last_ingestion_time(self):
        conn = get_connection()
        cur = conn.cursor()
        cur.execute("SELECT MAX(timestamp) FROM weather_data")
        result = cur.fetchone()[0]
        conn.close()
        return result
