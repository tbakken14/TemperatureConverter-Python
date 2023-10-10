CONSTRAINTS = {"F" : -459.67, "C" : -273.15, "K" : 0}

def getValidInputs():
    fromUnit = getValidInput("Enter a unit to convert from: ", 
                                    validateUnit)
    toUnit = getValidInput("Enter a unit to convert to: ", 
                                  validateUnit)
    temperature = getValidInput(f"Enter temperature to convert from {fromUnit} to {toUnit} : ", 
                                     validateTemperature, 
                                     fromUnit)
    return [fromUnit, toUnit, temperature]

def getValidInput(prompt, _isValid, *args):
    input = getInput(prompt)
    while(not _isValid(input, *args)):
        input = getInput(prompt)
    return input

def getInput(prompt):
    print(prompt, end = "")
    return input()

def validateTemperature(temperature, unit):
    if not isFloat(temperature):
        print("\nTemperature is not a number\n")
        return False
    temperature = float(temperature)
    if temperature < CONSTRAINTS[unit]:
        print("\nTemperature is below absolute zero\n")
        return False
    return True
    
def validateUnit(unit, *args):
    if not unit in CONSTRAINTS:
        print("\nUnit is not valid\n")
        return False
    return True

def isFloat(str):
    return str.replace(".", "", 1).replace("-", "", 1).isdecimal()