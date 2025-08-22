abc = 'with three words'

split = abc.split() # .split() , splits a string into individual values, it produces a list of strings.

print(len(split)) # now instead of returning individual characters like it would for a string, its returning the values 

print(split[1])# and we can use the index method like we would a list

print(split)
for w in split: # we can now also loop through a string using split since it turns it to a list of strings
    print(split)


# second section of learning lists and strings
##.split()
print('=====================================================')

line = 'a lot                               of spaces'
split_line = line.split() # .split treats multiple spaces as just one space
print(split_line)

line = 'first;second;third' # since there is no spaces, we still return a list but it will only have a single value,
splitting = line.split()
print(splitting) # since split does not find any spaces it does not separate the values and only returns one value

splitting_line = line.split(';') # you can also specify what piece of value u want to split
print(splitting_line) # we basically said instead of using spaces by default to split, use ';' as the splitting value


