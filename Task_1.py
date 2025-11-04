'''Task: String Reversal
Create a Python function that takes a
string as input and returns the reverse of
that string. For example, if the input is
"hello,
" the function should return
"olleh.
"'''

def reverse():
    s = input("Enter a string:")
    s1 = s[::-1]
    return s1

print(reverse())

