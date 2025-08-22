handle = open('mbox.txt')

for line in handle:
    line = line.rstrip()
    #print('line ', line) # debug
    word = line.split()
    #print('words ', word) #debug
     #guardian
    if len(word) < 3 or word[0] != 'From': # remember the debug(guardian) comes first
        #print('ignore') #debug
        continue
    print(word[2])