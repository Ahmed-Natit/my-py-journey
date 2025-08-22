names = dict()

names ['ahmed'] = 1
names['arwa'] = 1

print(names)

names['ahmed'] = names['ahmed'] + 1 # add one to the value in the key 'ahmed'
print(names)

#second section of learning counting dictionaries 
# histogram code
print('=======================================================')
counts = dict()
names = ['ahmed', 'muhajer', 'arwa', 'ismael', 'ahmed']

for name in names:# for every name in names
    if name not in counts: #  if the name is not found in count
        counts[name] = 1 # than add it to the dictionary (in other words appending the key to counts)
    else:
        counts[name] = counts[name] + 1 # if the name(key) is in counts already than return the name plus 1 
print(counts)

#sub section 
#collapse the histogram code into a few lines with .get()
print('==========================================================')

for name in names:
    counts[name] = counts.get(name, 0) + 1 # .get() method is  a method to check if a key is in the dictionary 
# the .get() method gives us default value of 0, so when were checking if something is in a dictionary we can just add 1 to that default value
print(counts)