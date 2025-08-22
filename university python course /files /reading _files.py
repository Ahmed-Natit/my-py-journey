handle = open('mbox.txt') # open is function that allows us to open a file 
for lines in handle: # for each line in handle 
    print(lines) # itl print each line



# second section of learning files 
##counting lines in a file 
print('======================================================================================================')

count_handle = open('mbox.txt')
count = 0
for line in count_handle:
    count = count + 1
print('line count :', count)



#third section of learning files
##reading te whole file 
print('======================================================================================================')

read_handle = open('mbox.txt')
reader = read_handle.read() # .read() reads the file 
print(len(reader)) # returns the read total length of the file
print(reader[:20]) # returns the read file at the specified index positions



#fourth section of learning files
##searching through the whole file 
print('======================================================================================================')

whole_handle = open('mbox.txt')
for line in whole_handle: # for every line in the file
    if line.startswith('From:'): # if the line startswith this specific string
        print(line) # print that line

#fix new line issue 
print('================================')
strip_handle = open('mbox.txt')

for line in strip_handle:
    line = line.rstrip() #rstrip is another way of stripping the white space 
    if line.startswith('From:'):
        print(line) #  strip the white space 



#fifth section of learning files
##skipping through lines
print('======================================================================================================')

skip_handle = open('mbox.txt')

for line in skip_handle:
    line = line.rstrip()
    if not '@uct.ac.za' in line: # if its not this string than just skip it
        continue # skip it
    print(line) # it will only print what ever line that was not skipped meaning, any line with '@uct.ac.za' will print




#sixth section of learning files
##apply same logic to any files using 'input'
#print('======================================================================================================')

#input_handle = input('enter a file: ')

#open_input = open(input_handle)

#count = 0
#for line in input_handle:
#    if line.startswith('Subjects: '):
#        count = count + 1
#print('there where', count, 'subject lines in', input_handle)




#seventh section of learning files
## using try and except in the event input is null

print('======================================================================================================')

null_handle = input('enter a file: ')

try:
    open_null = open(null_handle) # try to open the file that was inputted
except:
    print("no such file or file cannot be opened:", null_handle) # if it does not work than print this and quit the program
    quit() # quit the program 

#only if try is true than this will run 
for line in null_handle:
    if line.startswith('Subjects:'):
        count = count + 1
print('there where', count, 'subject lines in', null_handle)
    
