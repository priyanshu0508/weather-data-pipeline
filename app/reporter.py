# import json
# import os
# from monitor import pipeline_health_check

# def generate_status_dashboard():
#     status = pipeline_health_check()

#     os.makedirs("reports", exist_ok=True)

#     with open("reports/status.json", "w", encoding="utf-8") as f:
#         json.dump(status, f, indent=4)

#     return status


import os
import json
from database import get_connection
from monitor import pipeline_health_check

# -----------------------------
# Weather analytics report
# -----------------------------
def generate_weather_report():
    os.makedirs("reports", exist_ok=True)

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT 
            COUNT(*) as total_records,
            AVG(temperature),
            MIN(temperature),
            MAX(temperature),
            AVG(humidity)
        FROM weather_data
    """)

    row = cursor.fetchone()
    conn.close()

    if not row or row[0] == 0:
        report = (
            "Weather Summary Report\n"
            "----------------------\n"
            "No data available yet.\n"
        )
    else:
        total, avg_temp, min_temp, max_temp, avg_humidity = row
        report = f"""
Weather Summary Report
----------------------
Total Records: {total}

Average Temperature: {avg_temp:.2f} °C
Minimum Temperature: {min_temp:.2f} °C
Maximum Temperature: {max_temp:.2f} °C

Average Humidity: {avg_humidity:.2f} %
""".strip()

    with open("reports/weather_report.txt", "w", encoding="utf-8") as f:
        f.write(report)


# -----------------------------
# Pipeline health dashboard
# -----------------------------
def generate_status_dashboard():
    os.makedirs("reports", exist_ok=True)

    status = pipeline_health_check()

    with open("reports/status.json", "w", encoding="utf-8") as f:
        json.dump(status, f, indent=4)
