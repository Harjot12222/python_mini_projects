import string

password = input("Please enter the password: ")
score = 0

# Conditions
has_upper = any(ch.isupper() for ch in password)
has_lower = any(ch.islower() for ch in password)
has_special = any(c in string.punctuation for c in password)
has_digit = any(ch.isdigit() for ch in password)
has_length = len(password) >= 8

# Score calculation
all_conditions = [has_upper, has_lower, has_special, has_digit, has_length]
score = sum(all_conditions)  # True counts as 1

# Strength evaluation
if score <= 2:
    print("The password strength is WEAK ❌")
elif 3 <= score <= 4:
    print("The password strength is MEDIUM ⚠️")
else:
    print("The password strength is STRONG ✅")

print("Final score:", score)
