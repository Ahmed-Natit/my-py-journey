first = "ahmed"
last = "natit"
full = f"{first} {last}"
# 🔹 f-strings let you embed variables or expressions inside a string using {}
full2 = f"{len(first)} {2 + 3}"
print(full)
print(full2)
# 🔹 f-strings are a cleaner way to combine variables with line breaks: f"{var1}\n{var2}
# 🔹 f"{name}" inserts the value of `name`
# 🔹 f"{len(name)}" runs the function and shows the result
# 🔹 f"{2 + 3}" runs the math inside the braces
