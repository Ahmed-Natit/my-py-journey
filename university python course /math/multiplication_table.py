num = int(input("What multiplication table would you like: "))
print("====================================================")
print(f"Multiplication Table of {num}:\n")

for i in range(1, 13):
    print(f"{num} x {i} = {num * i}")