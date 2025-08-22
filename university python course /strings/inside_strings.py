fruit = 'banana'
letter = fruit[1] # "[]" is an index operator, the index here is the position of each letter in fruit
print(letter)# will just print "a" since the index of a in the 'banana' is 1

x = 3
w = fruit[x - 1]# since x = 3, 3 - 1 = 2, this will return "n" since n is the second index in the string 'banana'
print(w)

print(len(fruit))#  this will print out the length of our string 


## second section of learning strings

print('=====================================================================================================')
index = 0

#while loop
while index < len(fruit):# while the index is less than the len of 'banana'(6)
    letter = fruit[index]# letter is equal to the position of the letter at index position 
    print(index, letter) # this will print the position of the letters and the letter individually through each iteration 
    index = index + 1

print('==============')
# for loop
for letter in fruit: # for every letter in fruit(a piece of string )
    print(letter)# print every string in that piece of string


##third section of learning strings

print('============================================================================')

#count how many 'a' there are
count = 0
for letter in fruit: # fruit is 'banana' and there is 3 a's
    if letter == 'a': # if one of those values(letters) are 'a'
        count = count + 1 # than count goes up by 1
print(count, "number of a's")



# fourth section of learning strings

print('============================================================================')

s  = 'Monty Python'
print(s[0:4]) # start at position 0 and go up to 4 but not including 4 (should return from M:0 to T:3, total returns 'Mont')
print(s[6:7])# starts from 6 up to 7 but nor including 7 and since the 6th position is 'P' we return 'P'

print(s[6:20]) # starts at 6 than goes all the way at the end and since there is nothing above 11, it will just return the full string just starting from where u specified 


# fifth section of learning strings

print('============================================================================')

pos = fruit.find('na')# .find method goes inside the string and finds the pieces of string we want 
print(pos)

aa= fruit.find('z')
print(aa)



