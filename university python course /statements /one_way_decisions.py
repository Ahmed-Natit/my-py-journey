x = 5

print('before 5') 
if x == 5: # this is true
    print('it is 5') # since it is true it will print
    print('it is still 5') # since it is true it will print
    print('third 5') # since it is true it will print

print('afterwards is 5')

print('before 6')

if x == 6: # this is false 
    print('it is 5') # since it is false this will not print 
    print('it is still 5') # since it is false this will not print 
    print('third 5') # since it is false this will not print 

print("afterwards is 6") # but this will print because it is outside of the if statement indentation
    