'''Task: Calculator Program
Create a Python program that acts as a basic
calculator. It should prompt the user to
enter two numbers and an operator (+
, -,
*
, /,
%), and then display the result of the
operation. '''
print("---Basic Calculator---")
op = input("Enter an Operator to perform Operations(+,-,*,/): ")

if op == "+":
    a = int(input("Enter 1st number: "))
    b = int(input("Enter 2nd number: "))
    s = a+b
    print(f"The sum of {a} and {b} is:", s)
elif op == "-":
    a = int( input( "Enter 1st number: " ) )
    b = int( input( "Enter 2nd number: " ) )
    s = a - b
    print(f"The Subtraction of {a} and {b} is:", s)
elif op == "*":
    a = int( input( "Enter 1st number: " ) )
    b = int( input( "Enter 2nd number: " ) )
    s = a * b
    print(f"The multiplication of {a} and {b} is:", s)
elif op == "/":
    a = int( input( "Enter 1st number: " ) )
    b = int( input( "Enter 2nd number: " ) )
    s = a / b
    print(f"The division of {a} and {b} is:", s)
else:
    print("Invalid operations, Try again later!")

