print('before')
for thing in [9, 41, 12, 3, 74, 15]:
    print(thing)
print('after ')

# second section of learning loop idioms

#finding the largest number from a list
print('=================================================')

largest_num = 0 # the 0 is just there as a random value

print('before loop', largest_num)  # showing tus the number before loop

for number in [9, 41, 12, 3, 74, 15]: # for every number in this list
    if number > largest_num: # if the number is greater than 0
        largest_num = number # than largest number will be equal to that number 
    print(largest_num, number)# than we print both numbers the numbers in the list along side the largest number

print('the largest number after loop:', largest_num)# gives us back the largest number 
