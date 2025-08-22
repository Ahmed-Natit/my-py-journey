#!/bin/python3

num1 = float (input("enter first number:"))
operation = input("enter operation: ")
num2 = float (input("enter second number:"))

if operation == "+":
    result = num1 + num2
elif operation == "-":
    result = num1 - num2
else:
    print("Invalid operation.")
    result = None

if result is not None:
    print("result:", result)











    
