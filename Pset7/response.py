import validators

test=str(input("What's your email address? "))


if validators.email(test):
    print("Valid")
else:
    print("Invalid")
