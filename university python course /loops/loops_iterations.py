n =5 
while n > 0: #once n is 0 the loop will end 
    print(n) 
    n = n - 1 # going down by 1 each time n is greater than 0

print('blastoff') # these 2 print statement will always print
print(n)

## second part of learning loops

print('================================================================')

while True:
    line = input('> ')
    if line == 'done':
        break
    print(line)
print('done !')   

## third part of learning loops

print('================================================================')

while True:
    line_2 = input('> ')
    if line_2 == '#':
        continue
    if line_2 == 'done':
        break
    print(line_2)
print('done !')
