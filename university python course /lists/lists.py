mutable_list = [23, 33, 44, 55, 66]
print('before change', mutable_list)
mutable_list[0] = 22
print('after change',mutable_list)

# second section learning lists
## len of strings vs len of lists
print('===========================================================')

string = 'asalamu alaikum'
string_list = ['me', 'you', 'race', '4'] # 4 values in this list
print(len(string)) # will print out the amount of characters 

print(len(string_list)) # will print our the amount of values in the list instead of characters


# third section learning lists
## range()
print('===========================================================')

print(range(4)) # will print a range from 0 to 4 

print(range(len(string_list))) # will print the range of the len of the list, if list has 4 than it will print 0 to 4


# sub section 
print('=======')

friends = ['jj', 'ismael', 'muhajer']

# 'i' is 0 in the first iteration which in the len(friends) is 'jj', in the next it goes to 1 which is 'ismael' and so on
for i in range(len(friends)): 
    friend = friends[i] # so here when we use the index method for the list, its just calling that value in the position 'i'
    print('good day', friend)