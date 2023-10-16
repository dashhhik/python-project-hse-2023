document.addEventListener("DOMContentLoaded", function() {
    const cityName = getCityFromUrl();
    fetch(`/api/weather/current/${cityName}/days/`)
        .then(response => response.json()
        )
        .then(data => {

            updateWeatherData(data);
        })

});

function getCityFromUrl() {
    const pathSegments = window.location.pathname.split('/');
    return pathSegments[3];
}


function updateWeatherData(weatherData) {
    try {
        weatherData = JSON.parse(weatherData);
        document.getElementById("city-name").innerText = weatherData.city.name;
        const weatherDetails = weatherData.list[0];
        document.getElementById("temperature").innerText = weatherDetails.main.temp;
        document.getElementById("feels-like").innerText = weatherDetails.main.feels_like;
        document.getElementById("description").innerText = weatherDetails.weather[0].description;
        document.getElementById("humidity").innerText = weatherDetails.main.humidity;
        document.getElementById("wind-speed").innerText = weatherDetails.wind.speed;
        document.getElementById("pressure").innerText = weatherDetails.main.pressure;
        document.getElementById("clouds").innerText = weatherDetails.clouds.all;

        const date = new Date(weatherDetails.dt * 1000);
        document.getElementById("time").innerText = date.toLocaleString("ru-RU");

    } catch (error) {
        console.error("Ошибка при обработке погодных данных:", error);
    }
}
