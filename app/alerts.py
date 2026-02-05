def check_weather_alerts(data):
    alerts = []
    if data["main"]["temp"] > 40:
        alerts.append("High temperature alert")
    if data["main"]["humidity"] > 90:
        alerts.append("High humidity alert")
    return alerts
