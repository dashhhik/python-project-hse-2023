import asyncio

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
                   f'&appid={api_key}&units=metric&cnt=4&lang=ru')
        async with session.get(api_url) as resp:
            json = await resp.json()

            whole_forecast = WeatherData(**json)
            return whole_forecast


#
# asyncio.run(get_zip_code_city("moscow"))

import requests

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/2.537.36',
}
url = "http://api.openweathermap.org/geo/1.0/direct?q=moscow&limit=1&appid=ff93ecd9453d372012f26751c5ddfa78"


def what_to_wear():
    pass
