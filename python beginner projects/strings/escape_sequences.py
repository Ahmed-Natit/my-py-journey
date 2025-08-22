# 👉 \" lets you include double quotes inside a double-quoted string
course = "python \"programming"

# 👉 \' lets you include single quotes inside a single-quoted string
course2 = 'python \'programming'

# 👉 \n adds a new line (line break) between words
course3 = "python \nprogramming"
# 👉 \\ prints a single backslash inside the string
course4 = "python \\programming"


print(course + "\n" + course2 + "\n" + course3 + "\n" + course4)
# 🔹 Use + to join strings and newline characters (\n)
# 🔹 f-strings are a cleaner way to combine variables with line breaks: f"{var1}\n{var2}"
print(f"{course}\n{course2}\n{course3}\n{course4}")
