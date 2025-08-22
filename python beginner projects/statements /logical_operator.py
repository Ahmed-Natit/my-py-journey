high_income = False
good_credit = True
student = False
# Using the 'and' operator to check if both conditions are true

if (high_income or good_credit) and not student:
    print("Eligible")
else:
    print("Not Eligible")
# Using the 'or' operator to check if at least one condition is true
