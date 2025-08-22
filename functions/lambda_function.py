def double(x): return x * 2
def add(x, y): return x + y
def max_value(x, y): return x if x > y else y
def min_value(x, y): return x if x < y else y
def full_name(first, last): return first + "" + last
def is_even(x): return x % 2 == 0
def age_check(age): return "Adult" if age >= 18 else "Minor"


print(age_check(20))
print(age_check(16))
print(full_name("John ", "Doe"))
print(is_even(5))
print(min_value(5, 6))
print(max_value(5, 4))
print(add(5, 5))
print(double(5))
# This is a simple lambda function that doubles the input value.
