from fastapi import APIRouter
from .api.api_services import get_zip_code_city, get_weather_api


router = APIRouter()


@router.get("/weather/current/{city}/days/")
async def get_weather(city):
        location = await get_zip_code_city(city)
        weather_data = await get_weather_api(location)
        return weather_data



