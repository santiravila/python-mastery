import re


email = input("What's your email? ").strip()

pattern = r"^\w+@(?:\w|\.)?\w+\.edu$"
if re.search(pattern, email):
    print("Valid")
else:
    print("Invalid  ")

#username, domain = email.split("@")

#if (username) and (domain.endswith(".edu")):
#    print("Valid")
#else:
#    print("Invalid")