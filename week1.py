num1 = input("Enter first number: ")
num2 = input("Enter second number: ")
operation = input("Enter operation (+, -, *, /): ")

# Convert inputs to numbers
num1 = float(num1)
num2 = float(num2)

if operation == "+":
    result = num1 + num2
    print("Result:", result)
elif operation == "-":
    result = num1 - num2
    print("Result:", result)
elif operation == "*":
    result = num1 * num2
    print("Result:", result)
elif operation == "/":
    if num2 != 0:
        result = num1 / num2
        print("Result:", result)
    else:
        print("Cannot divide by zero.")
else:
    print("Invalid operation.")
