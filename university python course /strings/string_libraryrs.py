greet = 'HELLO BOB'
lower = greet.lower()# .lower() is a method that converts our string to lower case

print(lower)
print(greet)
print('HI THERE'.lower())


print('===================')

upper = greet.upper()# .upper() is a method that converts our string to upper case

print(upper)
print('hi there '.upper())


# second section of learning strings

print('============================================================================')

replace = greet.replace('BOB', 'JANE')# .replace(), replaces function goes and searches for the string, finds it and replaces it
print(replace)

replace = greet.replace('O', 'X') #  since we made it an upper case up above we have to use capital letters
print(replace)


#third section of learning strings

print('============================================================================')

whit_space = '    hello bob    '
print(whit_space.strip())


# fourth section of learning strings 

print('============================================================================')

line = 'Please have a nice day'
print(line.startswith('Please'))# this method checks if u started with a specific value 
print(line.startswith('p')) # lower case p will return false if line does not start with lower case p
