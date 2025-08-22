x = 5
print('hello')

def print_lyrics():
    print('itsy miny mo ')
    print('itsy itsy mo')
    print('miny miny mo')

print('itsy')
x = x + 2
print_lyrics() # we have called it here now it will work 
print(x)

#since we dont call the function we made (def) it will not run 
# only run when we call, print_lyrics() 


## second part of learning def
print('==================================================================')

def greet(lang):
    if lang == 'es':
        return 'hola' # return instead of print 
    elif lang == 'fr':
        return 'bonjour' # return instead of print
    else: 
        return 'hello' # return instead of print
    
language = input('what language u speak ?')

if language == 'espanol':
    print(greet('es')) # we have to print it when we call it, since the function just returns the string does not print it 
elif language == 'french':
    print(greet('fr'))
else:
    print(greet('english'))

##third part of learning def

#made  a function to add 2 numbers together 
print('=======================================================')
def add_these_two(a, b):
    added = a + b
    return added

print(add_these_two(3, 5))