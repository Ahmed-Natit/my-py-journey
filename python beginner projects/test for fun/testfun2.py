knows = {('son', 'father'): True, }

x = 'son'
y = 'father'

# This checks if x knows y, defaulting to False if not found in the dictionary, but since it is in the know dictionary that we made it will be true its only false if it isn't there.
# the get dictionary is a way to store relationships, in this case, who knows whom.
mind = knows.get((x, y), False)

# This negates the fact that x knows y by making it go from True to False using the not statement it goes from being true to not being true  .
not_mind = not mind

mind = True
not_mind = True

# This code checks if x knows y and if x does not know y, which is logically contradictory.
if mind and not_mind:
    print("Contradiction: x knows y AND x does NOT know y — invalid logic!")
    # IT WILL NEVER HAPPEN, IT WILL NEVER PRINT SOMETHING THATS TRUE AND FALSE AT THE SAME TIME
else:
    print("contradiction cannot be printed, both true and false and the same time, INVALID!")
    # COMPUTER SMARTER THAN CHRISTIANS
