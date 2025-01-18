FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5

def convert_to_celsius(fahrenheit):
    c = (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR
    return f"{fahrenheit}°F is {c}°C"

def convert_to_fahrenheit(celsius):
    c = (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32 
    return f"{celsius}°C is {c}°F"

temp = input("Enter the temperature to convert: ")
temp = int(temp)
f_c = input("Is this temperature in Celsius or Fahrenheit? (C/F):")

if f_c == "F":
    convert_to_celsius(temp)
elif f_c == "C":
    convert_to_fahrenheit(temp)
else:
    print("Invalid temperature. Please enter a numeric value.")

