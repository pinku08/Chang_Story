"""
Create a file called LastName_pythagorean.py. Write a program that will ask the user to
enter their name and respond with a greeting using this name.

Next your program will ask them to enter the lengths of the legs of a right triangle a and
b. We will use these to compute the length of the hypotenuse:

Compute the length of the hypotenuse and then return the result in a print statement.
(*Don’t only print the value, make sure you add both strings and floats in your statement).
"""

name=int(input('What is you name?:'))
print ("hello"+name)

from math import sqrt
print("Input lengths of shorter triangle sides:")
a = float(input("a: "))
b = float(input("b: "))

c = sqrt(a**2 + b**2)**(1%2)
print("The length of the hypotenuse is", c )





