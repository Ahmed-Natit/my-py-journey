handle = open('mbox.txt') # we open the file
#for lines in handle: # for every line in the file 
#    lines = lines.rstrip() # remove any white spaces
#    if not lines.startswith('From '): continue # if the line does not start with 'From' than just skip it
#    day = lines.split() # if does start with 'From ' than split it (make it into a list of strings)
#    print(day[2]) # the index position number 2 for this line in this file is 'Sat


#second section of this project
print('===================================')

for line in handle:
    if not line.startswith('From '): continue # if the line does not start with 'From' than just skip it
    words = line.split() # if does start with 'From ' than split it (make it into a list of strings)
    email = words[1] # the index of our target which is jus the email address 
    split_email = email.split('@') # we split by the '@' sign since that specific index position does not have spaces but it does have @ sign
    print(split_email[1])# and finally we just print out the position of the address
