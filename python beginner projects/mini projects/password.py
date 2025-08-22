import string

password = input("Enter your password: ")

# Check for special characters
has_special = any(char in string.punctuation for char in password)

# Determine strength based on length
if len(password) < 8:
    strength = "Weak"
elif len(password) < 15:
    strength = "Strong"
else:
    strength = "Very Strong"

# Add note if special characters are present
if has_special and len(password) >= 8:
    strength += " (contains special characters)"

# Check if password is only numbers
if password.isdigit():
    print("Password should not be only numbers. Please include letters and symbols.")
# Check if password is only letters
elif password.isalpha():
    print("Password should not be only letters. Please include numbers and symbols.")
# Check if password is all uppercase or all lowercase
elif password.isupper() or password.islower():
    print("Password should use a mix of uppercase and lowercase letters.")
else:
    print(f"Password strength: {strength}")
