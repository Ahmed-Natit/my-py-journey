data = 'From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008'

atpos = data.find('@')# go and find the @ sign in data
print(atpos) # print it

space_pos = data.find(' ',atpos) #  look for a space, starting from the @ sign, the second parameter for .find() is start from 
print(space_pos)


# so we return what ever there is from the @ position plus 1 so we start at the pos right after the @ sign and stopping at the space  
host = data[atpos+1 : space_pos]
print(host)
