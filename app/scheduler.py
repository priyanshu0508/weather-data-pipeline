import time
from etl_pipeline import run_etl
from reporter import generate_weather_report, generate_status_dashboard
from config import CITY_LIST

INTERVAL_SECONDS = 3600

def start_scheduler():
    while True:
        for city in CITY_LIST:
            run_etl(city)

        # Generate reports after each cycle
        generate_weather_report()
        generate_status_dashboard()

        time.sleep(INTERVAL_SECONDS)
