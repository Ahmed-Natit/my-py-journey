print("Calculator.")
num1 = input("Enter a number: ")
operator = input("enter operator: ")
num2 = input("Enter a number: ")

if operator == "+":
    result = float(num1) + float(num2)
elif operator == "-":
    result = float(num1) - float(num2)
elif operator == "*":
    result = float(num1) * float(num2)
elif operator == "/":
    if float(num2) == 0:
        result = "Error: Division by zero is not allowed."
    else:
        result = float(num1) / float(num2)
else:
    result = "Error: Invalid operator."

print("Result:", result)
