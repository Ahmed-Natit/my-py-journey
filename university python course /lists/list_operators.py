#Concatenating lists

a = [1, 2, 3]
b = [4, 5, 6]

c = a + b # adding both the list together makes them into one lists 
print(c)# printing c will print both values in one list 
print(a) # if we print a it'll print only the values in a 

#second section on learning list operators 
## list slicing 
print('=======================================================')
t = [9, 41, 12, 3, 74, 15]# there is 6 values here

print([t[1:3]]) #print the values in list starting from the the 1st position (41 is 1st pos and 9 is 0s pos) till the 2nd position (12)
# it stops at the 3rd position does not go above it 

print(t[0:4])

print(t[4:6])


#third section on learning list operators 
## list methods
print('=======================================================')

x = list()

#print(type(x)) # will return the type x is
#print(dir(x)) # will print all methods u can use for x


#fourth section on learning list operators 
##adding (appending) a value to an empty list using .append()
print('=======================================================')

empty = list() # made empty list

empty.append('hello') # adding 'hello' to empty list with .append()
empty.append('99')# adding '99' to empty list with .append()
print(empty)# printing the updated list


#fifth section on learning list operators 
##checking if something is in my list using 'in'
print('=======================================================')

my_list = [1, 9, 21, 10, 16]

print(9 in my_list) # this is basically like asking, is 9 in my list, and it will return true or false 
print(22 in my_list) #false
print(22 not in my_list) # true



#sixth section on learning list operators 
##sort method in list using '.sort()'
print('=======================================================')

friends = ['jj', 'ismael', 'muhajer']
friends.sort() # sort will arrange the names or numbers in a list and return them in there chronological order
print(friends)

#seventh section on learning list operators 
##built in functions and lists
print('=======================================================')

num = [3, 41, 12, 9, 74, 15]

print('amount of values: ',len(num)) # prints the len of num (the amount of values in num, since its a list)

print('total: ', sum(num)) # the total of everything in num
print('average: ',sum(num)//len(num)) # the average value in num. '//' rounds the divided answer

print('biggest value: ',max(num)) # the biggest value in num

print('smallest value: ',min(num)) # the smallest value in num



