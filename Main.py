from InputControl import *
from TemperatureConverter import *

TEMPERATURE_CONVERTER_MAP = {"F" : {"K" : fahrenheitToKelvin, "C" : fahrenheitToCelsius},
                 "C" : {"K" : celsiusToKelvin, "F" : celsiusToFahrenheit},
                 "K" : {"F" : kelvinToFahrenheit, "C" : kelvinToCelsius}}
def main():
    fromUnit, toUnit, fromTemperature = getValidInputs()
    toTemperature = TEMPERATURE_CONVERTER_MAP[fromUnit][toUnit](float(fromTemperature))
    print("%.2f %s = %.2f %s" % (fromTemperature, fromUnit, toTemperature, toUnit))

if __name__ == "__main__":
    main()