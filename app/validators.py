def validate_weather_data(data):
    temp = data["main"]["temp"]
    humidity = data["main"]["humidity"]

    if not (-50 <= temp <= 60):
        return False
    if not (0 <= humidity <= 100):
        return False
    if "dt" not in data:
        return False

    return True
