num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
operator = input("Choose the operation (+, -, *, /): ")

match operator:
    case "+":
        print(f"The result is {num1+num2}.")
    case "-":
        print(f"The result is {num1-num2}.")
    case "*":
        print(f"The result is {num1*num2}.")
    case "/":
        if num2 !=0:
            print(f"The result is {num1/num2}.")
        print("Cannot divide by zero.")