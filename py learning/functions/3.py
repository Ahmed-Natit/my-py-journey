#!/bin/python3

num1 = float(input("enter first number: "))
op = input("enter an operator: ")
num2 = float(input("enter a second number"))

if op == "+":
    print(num1 + num2)
elif op == "-":
    print(num1 - num2)
elif op == "x":
    print(num1 * num2)
elif op == "÷":
    print(num1 / num2)
else:
    print("invalid operator ")