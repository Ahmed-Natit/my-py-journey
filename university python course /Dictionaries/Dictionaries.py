items = dict()# creating empty dictionary 
items['ahmed'] = 23 # the key is ahmed the value is 23
items['muhajer'] = 42
items['salam'] = 90
print(items) # printing the now filled dictionary 

print(items['ahmed']) # we call the key and the value will be printed so this will print '23'

print(items['ahmed'] + 3) # we add 3 top it 

items['ahmed'] = items['ahmed'] + 3 # this will add 3 to the value 
print(items)


#second section of learning dictionaries
print('================================')

ddd = dict()
ddd['age'] = 21
ddd['course'] = 182
print(ddd)

ddd['age'] = 23 # this edit will override the value in the previous dict and update it
print(ddd)

#third section of learning dictionaries
#dictionary literal constants
print('================================')

pc = {'cpu': 7, 'ssd': 244, 'ram': 8 }
print(pc)# since we made it a constant it will print the dictionary keys and values, without needing to add them in later on

nothing = {}
print(nothing) # will just print '{}
