a_string = 'Hello bob'

try:
    a_string = int(a_string) # wont work since the variable is a string and letters
    print('done: ', a_string)
except:
    print("cannot convert a string into an integer")# output 


another_string = '123'

try:
    another_string = int(another_string) # will convert to an int, although it is a string its numbers, and numbers are integers.
    print('done: ', another_string)
except:
    print("cannot convert a string into an integer")