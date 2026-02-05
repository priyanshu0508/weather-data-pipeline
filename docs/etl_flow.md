## ETL Flow

Extract:
- Call OpenWeatherMap API

Transform:
- Validate temperature, humidity
- Normalize timestamps

Load:
- Insert into weather_data table
- Maintain referential integrity
