from database import create_tables
from scheduler import start_scheduler
from etl_pipeline import run_etl
from reporter import generate_weather_report, generate_status_dashboard
from config import CITY_LIST, CITY_NAME

def main():
    print("Initializing Weather Data Pipeline...")
    create_tables()

    if CITY_LIST:
        print("Running in scheduled multi-city mode")
        print("Press CTRL + C to stop the pipeline")
        start_scheduler()
    else:
        print(f"Running single ETL for city: {CITY_NAME}")
        run_etl(CITY_NAME)
        generate_weather_report()
        generate_status_dashboard()
        print("Pipeline execution completed")

if __name__ == "__main__":
    main()
