def kelvinToCelsius(temperature):
    return temperature - 273.15

def celsiusToKelvin(temperature):
    return temperature + 273.15

def celsiusToFahrenheit(temperature):
    return temperature * 1.8 + 32

def fahrenheitToCelsius(temperature):
    return (temperature - 32) * 5 / 9.0

def fahrenheitToKelvin(temperature):
    return fahrenheitToCelsius(celsiusToKelvin(temperature))

def kelvinToFahrenheit(temperature):
    return kelvinToCelsius(celsiusToFahrenheit(temperature))