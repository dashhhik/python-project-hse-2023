import asyncio
import json

import aiohttp
import requests

from .json_models import CoordsOfCity, WeatherData

api_key = "ff93ecd9453d372012f26751c5ddfa78"


async def get_zip_code_city(city) -> CoordsOfCity:
    async with aiohttp.ClientSession() as session:
        api_url = f"http://api.openweathermap.org/geo/1.0/direct?q={city}&limit=1&appid={api_key}"
        async with session.get(api_url) as resp:
            json = await resp.text()
            json = json[1:-1]
            coords = CoordsOfCity.model_validate_json(json)
            return coords


async def get_weather_api(coords: CoordsOfCity) -> WeatherData:
    async with aiohttp.ClientSession() as session:
        api_url = (f'http://api.openweathermap.org/data/2.5/forecast?lat={coords.lat}&lon={coords.lon}'
                   f'&appid={api_key}&units=metric&cnt=4&lang=en')
        async with session.get(api_url) as resp:
            json = await resp.json()
            print(json)

            whole_forecast = WeatherData(**json)

            return whole_forecast


def what_to_wear(weather_data: WeatherData):
    data_list = weather_data.list
    avg_feels_like = sum([entry.main.feels_like for entry in data_list]) / len(data_list)
    weather_conditions = [entry.weather[0].description for entry in data_list]
    wind_speeds = [entry.wind.speed for entry in data_list]
    humidity_levels = [entry.main.humidity for entry in data_list]
    cloudiness = [entry.clouds.all for entry in data_list]

    if avg_feels_like <= 0:
        recommendation = "Warm hat, gloves, scarf, warm down jacket or jacket, warm shoes."
    elif avg_feels_like <= 10:
        recommendation = "Light hat, warm sweater, demyson jacket, thick sole shoes."
    elif avg_feels_like <= 20:
        recommendation = "Sweater or light sweater, jeans or pants, sneakers."
    else:
        recommendation = "T-shirt, shorts, light shoes."

    if "rain" in weather_conditions:
        recommendation += " Don’t forget an umbrella or raincoat."
    if "cloudy" in weather_conditions and max(cloudiness) > 70:
        recommendation += " Might need a sweater or a jacket."
    if max(wind_speeds) > 5:
        recommendation += " Put on some windproof clothes."
    if max(humidity_levels) > 80:
        recommendation += " Don’t get your clothes wet."

    return recommendation


def get_recommendation_json(weather_data: WeatherData):
    recommendation = what_to_wear(weather_data)

    avg_temp = round(sum([entry.main.temp for entry in weather_data.list]) / len(weather_data.list))
    avg_feels_like = round(sum([entry.main.feels_like for entry in weather_data.list]) / len(weather_data.list))
    avg_humidity = round(sum([entry.main.humidity for entry in weather_data.list]) / len(weather_data.list))
    avg_wind_speed = round(sum([entry.wind.speed for entry in weather_data.list]) / len(weather_data.list))

    weather_conditions = [entry.weather[0].description for entry in weather_data.list]
    most_common_weather = max(set(weather_conditions), key=weather_conditions.count)

    result = {
        "city": weather_data.city.name,
        "country": weather_data.city.country,
        "average_temperature": avg_temp,
        "average_feels_like": avg_feels_like,
        "average_humidity": avg_humidity,
        "average_wind_speed": avg_wind_speed,
        "most_common_weather": most_common_weather,
        "recommendation": recommendation

    }

    json_result = json.dumps(result, ensure_ascii=False)

    return json_result
