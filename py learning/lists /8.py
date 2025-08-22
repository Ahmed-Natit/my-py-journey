#!/bin/python3

lucky_number = [4, 8, 16, 21, 43]
friends = ["khalid", "muhammed", "yaseen", "abdullah"]
friends .append("jj")
friends .extend(lucky_number)
friends .insert(1, "fahad")
friends .remove("yaseen")
friends .pop()
friends .reverse()
friends2 = friends.copy()

print(friends)

friend = ["tahir", "sultan"]

friend .clear()

bros = ["mobin", "mobin", "bilal"]

print(bros.count("mobin"))

mates = ["aman", "sulaiman", "bilal"]
mates.sort()
print(mates)
