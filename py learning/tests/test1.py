#!/bin/python3

num1 = float(input("enter the first number: "))
op = input("enter a operator: ")
num2 = float(input("enter your second number: "))

if op == "+":
   print(num1 + num2)

elif op == "-":
     print(num1 - num2)

elif op == "*":
     print(num1 * num2)

elif op == "/":
      print(num1 / num2)

else:
    print("invalid operator")
