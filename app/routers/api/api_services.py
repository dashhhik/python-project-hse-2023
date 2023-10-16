import aiohttp
from .json_models import CoordsOfCity, WeatherData

api_key = "ff93ecd9453d372012f26751c5ddfa78"


async def get_zip_code_city(city) -> CoordsOfCity:
    async with aiohttp.ClientSession() as session:
        api_url = f"http://api.openweathermap.org/geo/1.0/direct?q={city}&limit={1}&appid={api_key}"
        async with session.get(api_url) as resp:
            json = await resp.text()
            json = json[1:-1]
            coords = CoordsOfCity.model_validate_json(json)
            return coords


async def get_weather_api(coords: CoordsOfCity) -> WeatherData:
    async with aiohttp.ClientSession() as session:
        api_url = (f'http://api.openweathermap.org/data/2.5/forecast?lat={coords.lat}&lon={coords.lon}'
                   f'&appid={api_key}&units=metric&cnt=1&lang=ru')
        async with session.get(api_url) as resp:
            json = await resp.json()
            weather_data = WeatherData(**json)
            return weather_data
