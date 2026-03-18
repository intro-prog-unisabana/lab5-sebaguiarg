from utils_calc import *
resultdo = None
while True:
    operation = input("Which calculation would you like to perform? (add, subtract, multiply, divide, exponent, modulo, floor_divide, absolute, exit):").lower()
    print(operation)
    if operation == "add":
        num1 = int(input("Enter the first number:"))
        num2 = int(input("Enter the second number:"))
        resultdo = (add(num1,num2))
        print(f"The result is: {resultdo}")
    elif operation == "subtract":
        num1 = int(input("Enter the first number:"))
        num2 = int(input("Enter the second number:"))
        resultdo = (sub(num1,num2))
        print(f"The result is: {resultdo}")
    elif operation == "multiply":
        num1 = int(input("Enter the first number:"))
        num2 = int(input("Enter the second number:"))
        resultdo = (multiply(num1,num2))
        print(f"The result is: {resultdo}")
    elif operation == "divide":
        num1 = int(input("Enter the first number:"))
        num2 = int(input("Enter the second number:"))
        if num2 != 0:
            resultdo = (divide(num1,num2))
            print(f"The result is: {resultdo}")
        else:
            print("Error: Division by zero is not allowed.")
        
    elif operation == "exponent":
        num1 = int(input("Enter the first number:"))
        num2 = int(input("Enter the second number:"))
        resultdo = (exponent(num1,num2))
        print(f"The result is: {resultdo}")
    elif operation == "modulo":
        num1 = int(input("Enter the first number:"))
        num2 = int(input("Enter the second number:"))
        if num2 != 0:
            resultdo = (modulo(num1,num2))
            print(f"The result is: {resultdo}")
        else:
            print("Error: Modulo by zero is not allowed.")
    elif operation == "floor_divide":
        num1 = int(input("Enter the first number:"))
        num2 = int(input("Enter the second number:"))
        resultdo = (floor_divide(num1,num2))
        print(f"The result is: {resultdo}")
    elif operation == "absolute":
        num1 = int(input("Enter the first number:"))
        resultdo = (absolute(num1))
        print(f"The result is: {resultdo}")
    elif operation == "exit":
        break
    else: #Ninguna opcion fue elegida
        print("Invalid option!")