count = 0
print('before', count)

for value in [9, 41, 12, 3, 74, 15]:
    count = count + 1 # we add one each time through the loop
    print(count, value) # than we print how many time its gone through the loop based on (count = count + 1) and print the values in he list

print('after', count)# than we print the total amount of iterations 

# second section of learning loop patterns
print('==========================================================================================')
total = 0
print('before', total)

for value in [9, 41, 12, 3, 74, 15]: # we start at 9, so total becomes 9 on the first iteration based on the code below (total = total + value)
    total = total + value # on the second iteration when total = 9 it adds that to 41 since its the second value in the list
    print(total, value) # we than just return 0 + 9 = 9 than 9 + 41 than 50 + 12 ext, basically adds all the numbers together
print('after', total)


#third section of learning loop patters 
print('=============================================================================================')

count_avrg = 0
total_avrg = 0 
print('before', count_avrg, total_avrg)

for value in [9, 41, 12, 3, 74, 15]:
    count_avrg = count_avrg + 1 # counting iterations 
    total_avrg = value + total_avrg # finding the total 
    print(count_avrg, value, total_avrg) #printing them 

# we than print out both the the count and total and to get the avrg we divide both of them by each other 
print('after', count_avrg, total_avrg, total_avrg // count_avrg) # double // rounds it up tot he nearest number



# fourth section for learning loop patterns

print('=================================================================================================')

print('before')
for value in [9, 41, 12, 3, 74, 15]:
    if value > 20:# this loop will go through each of this values until it finds a number greater than 20 
        print('largest number', value) # if number greater than 20 found than print that as the largest value

print('after')


# fifth section of learning loop patterns 

print('=================================================================================================')

found = False # default is false since we haven't found our value yet
print ('before', found)

for value in [9, 41, 12, 3, 74, 15]:
    if value == 3: # if the value is 3 which is the value were looking for 
        found = True #  found is now true since that was the value we were looking for
    else:# we made it better with this else
        found = False # other wise for the other values, there false since there not what where looking for 
    print(found, value) # than print the if the value were looking for is found in the values

print('after', found) 


#sixth section of learning loop patterns
print('=================================================================================================')

smallest_so_far = None # none is a constant that indicates emptiness 
print('before')

for value in [9, 41, 12, 3, 74, 15]:
    # the smallest number will be none since its like that by default
    if smallest_so_far is None: # "is", is stronger than "=="
      smallest_so_far = value # after determining if smallest so far is none we set it equal to the value
    elif value < smallest_so_far: # if the value is less than the smallest number
        smallest_so_far = value # we set smallest number is equal to the value
    print(smallest_so_far, value)
print('after', smallest_so_far)

#end