def increment(number, by):
    return number + by


print(increment(2, by=1))

#setting a default value
def increment_2(number, by=5):
    return number + by


print(increment_2(2))
