import logging
from datetime import datetime
from api_client import fetch_weather
from validators import validate_weather_data
from database import get_or_create_city
from db.factory import get_db_client
from alerts import check_weather_alerts

logging.basicConfig(filename="logs/pipeline.log", level=logging.INFO)

def run_etl(city):
    raw = fetch_weather(city)

    if not validate_weather_data(raw):
        logging.error("Validation failed")
        return

    city_id = get_or_create_city(city)

    data = (
        city_id,
        raw["main"]["temp"],
        raw["main"]["humidity"],
        raw["main"]["pressure"],
        raw["weather"][0]["description"],
        datetime.utcfromtimestamp(raw["dt"]).isoformat()
    )

    for alert in check_weather_alerts(raw):
        logging.warning(alert)

    db = get_db_client()
    db.insert_weather(data)

    logging.info(f"ETL completed for {city}")
