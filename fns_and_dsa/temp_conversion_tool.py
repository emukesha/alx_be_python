
FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5

temp = input("Enter the temperature to convert: ")
temp = int(temp)
f_c = input("Is this temperature in Celsius or Fahrenheit? (C/F): ")

def convert_to_celsius(fahrenheit):
    c = FAHRENHEIT_TO_CELSIUS_FACTOR * int(temp)
    return f"{temp}°F is {c}°C"

def convert_to_fahrenheit(celsius):
    c = CELSIUS_TO_FAHRENHEIT_FACTOR * int(temp)
    return f"{temp}°C is {c}°F"

if f_c == "F":
    convert_to_celsius(temp)
elif f_c == "C":
    convert_to_fahrenheit(temp)
else:
    print("Invalid temperature. Please enter a numeric value.")

