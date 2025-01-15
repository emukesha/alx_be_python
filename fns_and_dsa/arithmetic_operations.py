
def perform_operation(num1, num2, operation):
    if operation == "add":
        output = num1 + num2
    elif operation == "subtract":
        output = num1 - num2
    elif operation == "multiply":
        output = num1 * num2
    elif operation == "divide":
        if num2 == 0:
            return "Can't divide with 0"
        else:
            output = num1/num2
