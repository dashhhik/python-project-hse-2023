document.addEventListener("DOMContentLoaded", function() {
    const cityName = getCityFromUrl();
    fetch(`/api/weather/clothes/current/${cityName}/days/`)
        .then(response => response.json()
        )
        .then(data => {

            updateWeatherData(data);
        })

});

function getCityFromUrl() {
    const pathSegments = window.location.pathname.split('/');
    return pathSegments[4];
}


function updateWeatherData(weatherData) {
    try {
        weatherData = JSON.parse(weatherData);
        document.getElementById("city-name").innerText = weatherData.city;
        document.getElementById("temperature").innerText = weatherData.average_temperature;
        document.getElementById("feels-like").innerText = weatherData.average_feels_like;
        document.getElementById("recommendation").innerText = weatherData.recommendation;
        document.getElementById("humidity").innerText = weatherData.average_humidity;
        document.getElementById("wind-speed").innerText = weatherData.average_wind_speed;

        document.getElementById("weather").innerText = weatherData.most_common_weather;



    } catch (error) {
        console.error("Ошибка при обработке погодных данных:", error);
    }
}
