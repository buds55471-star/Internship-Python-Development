'''Task: Palindrome Checker
Write a Python function that checks whether a given
string is a palindrome.A palindrome is a word, phrase, or sequence that reads the
same backward as forward( e.g., "madam" or "racecar" ).'''

def is_palindrome():
    forward = input("Enter a string:")
    backward = forward[::-1]
    if forward == backward:
        print("String is Palindrome")
    else:
        print("String is not Palindrome")
is_palindrome()
