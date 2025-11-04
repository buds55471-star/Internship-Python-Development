'''Task: Email Validator
Develop a Python function that validates whether a given string is a valid email address.
Implement checks for the format,including the presence of an "@" symbol and a domain
name'''

def check_email():
    email = input("Enter your Email: ")
    if "@" in email and "." in email.split("@")[-1]:
        print("The Email address looks valid.")
    else:
        print("Please enter a valid Email address with '@' and a domain name.")

check_email()

