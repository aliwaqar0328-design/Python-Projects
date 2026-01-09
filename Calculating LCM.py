"""

###    The smallest number that both the two numbers can divide is called LCM
###                For example LCM of 6 and 8 is 24
Formula = (a*b) =  GCD(a,b)*LCM(a,b)
LCM = (a*b)/GCD(a,b)
"""
import math

def calc_lcm(a,b):
    gcd = math.gcd(a,b)
    lcm = (a * b) // gcd
    return lcm

a = int(input("Enter your first number: "))
b = int(input("Enter your second number: "))

lcm = calc_lcm(a,b)

print(f"The LCM of {a} and {b} is {lcm}")

