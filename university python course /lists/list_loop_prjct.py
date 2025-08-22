num = list()

while True:
    inpt = input('Enter a number: ')
    if inpt == 'done': break # if the input is 'done' break (get out of loop) and than it will pint our avrg
    value = float(inpt)# we make it into a float since were working with division 
    num.append(value) # we append the values into the empty list 

print(sum(num) // len(num)) # returns the average in num 

