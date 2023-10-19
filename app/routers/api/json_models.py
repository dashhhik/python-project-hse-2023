from pydantic import BaseModel
from typing import List


class CoordsOfCity(BaseModel):
    lat: float
    lon: float
    country: str
    name: str
    state: str


class Weather(BaseModel):
    id: int
    main: str
    description: str
    icon: str


class Main(BaseModel):
    temp: float
    feels_like: float
    temp_min: float
    temp_max: float
    pressure: int
    sea_level: int
    grnd_level: int
    humidity: int
    temp_kf: float


class Clouds(BaseModel):
    all: int


class Wind(BaseModel):
    speed: float
    deg: int
    gust: float


class ListData(BaseModel):
    dt: int
    main: Main
    weather: List[Weather]
    clouds: Clouds
    wind: Wind
    visibility: int
    dt_txt: str


class Coord(BaseModel):
    lat: float
    lon: float


class City(BaseModel):
    id: int
    name: str
    coord: Coord
    country: str
    population: int
    timezone: int
    sunrise: int
    sunset: int


class WeatherData(BaseModel):
    cod: str
    message: int
    cnt: int
    list: List[ListData]
    city: City

