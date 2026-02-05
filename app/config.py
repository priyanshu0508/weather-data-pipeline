import os
from dotenv import load_dotenv

load_dotenv()

OPENWEATHER_API_KEY = os.getenv("OPENWEATHER_API_KEY")

CITY_NAME = os.getenv("CITY_NAME")
CITY_NAMES = os.getenv("CITY_NAMES", "")
CITY_LIST = [c.strip() for c in CITY_NAMES.split(",") if c.strip()]

BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

DATABASE_NAME = "data/weather.db"
LOG_FILE = "logs/pipeline.log"

DB_TYPE = os.getenv("DB_TYPE", "sqlite")

POSTGRES_CONFIG = {
    "dbname": os.getenv("PG_DB"),
    "user": os.getenv("PG_USER"),
    "password": os.getenv("PG_PASSWORD"),
    "host": os.getenv("PG_HOST"),
    "port": os.getenv("PG_PORT"),
}

if not OPENWEATHER_API_KEY:
    raise ValueError("OPENWEATHER_API_KEY missing")
