def safe_divide(numerator, denominator):
    try:
        numerator = float(numerator)
        denominator = float(denominator)
    except:
        return "Error: Please enter numeric values only."
        return
    try:
        return f"The result of the division is {numerator/denominator}"
    except:
        return "Error: Cannot divide by zero."