course = "python programming"
Email = """ 
hi john, hope you are doing well.

I wanted to let you know that I have completed the project we discussed last week.
"""
print(len(course))  # 👉 prints the total number of characters in the string (including space)
print(course[0])  # 👉 prints the first character: 'p'
print(course[-1])  # 👉 prints the last character: 'g'
# 👉 prints characters from index 0 to 2 (not including 3) → 'pyt'
print(course[0:3])
print(course[0:])  # 👉 prints from index 0 to the end → full string
print(course[:3])  # 👉 prints from the start to index 2 → same as [0:3]
# 👉 prints the entire string → same as saying "from start to end"
print(course[:])


# print(len(course))       # 👉 prints the total number of characters in the string (including space)

# print(course[0])         # 👉 prints the first character: 'p'

# print(course[-1])        # 👉 prints the last character: 'g'

# print(course[0:3])       # 👉 prints characters from index 0 to 2 (not including 3) → 'pyt'

# print(course[0:])        # 👉 prints from index 0 to the end → full string

# print(course[:3])        # 👉 prints from the start to index 2 → same as [0:3]

# print(course[:])         # 👉 prints the entire string → same as saying "from start to end"
