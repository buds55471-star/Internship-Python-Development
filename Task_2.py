'''Task: Temperature Conversion
Create a Python program that converts
temperatures between Celsius and
Fahrenheit. Prompt the user to enter a
temperature value and the unit of
measurement, and then display the
converted temperature. '''

def c_to_f():
    c = int(input(f"Enter temperature in celsius (℃): "))
    f = (c*9/5)+32
    print(f"The temperature of celsius in fahrenheit is {f}℉")

c_to_f()
