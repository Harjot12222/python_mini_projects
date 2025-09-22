import string

# Common spam keywords
common_spam = ["free", "win", "cash", "lottery", "prize", "offer", "unlimited"]

# User input
email = input("Please enter the email to check: ").lower()

# Remove punctuation and split into words
text = [w.strip(string.punctuation) for w in email.split()]

# Count spam indicators
found = [word for word in text if word in common_spam]
count = len(found)

if count >= 2:
    print(f"⚠️ Found {count} spam indicators: {', '.join(found)}")
    print("This email is likely SPAM.")
elif count == 1:
    print(f"⚠️ Found 1 spam indicator: {found[0]}")
    print("This email may be spam.")
else:
    print("✅ No spam indicators found. Email looks safe.")
