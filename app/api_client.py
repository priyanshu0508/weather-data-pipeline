import requests
from config import BASE_URL, OPENWEATHER_API_KEY

def fetch_weather(city):
    response = requests.get(
        BASE_URL,
        params={
            "q": city,
            "appid": OPENWEATHER_API_KEY,
            "units": "metric"
        },
        timeout=10
    )

    if response.status_code != 200:
        raise Exception(response.text)

    return response.json()
