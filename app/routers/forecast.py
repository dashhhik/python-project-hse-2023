from fastapi import APIRouter
from .api.api_services import get_zip_code_city, get_weather_api, get_recommendation_json
from fastapi.templating import Jinja2Templates
from fastapi import Request

router = APIRouter()

templates = Jinja2Templates(directory="./templates")


@router.get("/api/weather/current/{city}/days/")
async def get_weather(city):
    location = await get_zip_code_city(city)
    weather_data = await get_weather_api(location)
    return weather_data.model_dump_json()


# return templates.TemplateResponse("weather.html", {"request": dict(weather_data)})

@router.get("/weather/current/{city}/days/")
async def get_weather(request: Request):
    return templates.TemplateResponse("weather.html", {"request": request})


@router.get("/weather/clothes/current/{city}/days/")
async def get_clothes_(request: Request):
    return templates.TemplateResponse("clothes.html", {"request": request})


@router.get("/api/weather/clothes/current/{city}/days/")
async def get_weather(city):
    location = await get_zip_code_city(city)
    weather_data = await get_weather_api(location)
    cloth = get_recommendation_json(weather_data)

    return cloth
