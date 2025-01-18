
FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5

def convert_to_celsius():
    temp = input("Enter the temperature to convert: ")
    f_c = input("Is this temperature in Celsius or Fahrenheit? (C/F): ")
    if f_c == "F":
        c = int(temp) * FAHRENHEIT_TO_CELSIUS_FACTOR
    else:
        print("Invalid temperature. Please enter a numeric value.")
    return f"{temp}°F is {c}°C"

def convert_to_fahrenheit():
    temp = input("Enter the temperature to convert: ")
    f_c = input("Is this temperature in Celsius or Fahrenheit? (C/F): ")
    if f_c == "C":
        c = int(temp) * CELSIUS_TO_FAHRENHEIT_FACTOR
    else:
        print("Invalid temperature. Please enter a numeric value.")
    return f"{temp}°C is {c}°F"

