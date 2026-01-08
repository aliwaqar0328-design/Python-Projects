"""
     We can do this by importing math 
import math
a = 12
b = 15
print(math.gcd(a,b))
but we will try to do this with eculidean algorithm
it is recomended to google the concept of this algorithm first to have better understanding of how
our program is working!!!!!
"""
a = 12
b = 36

def calc_gcd(num1,num2):
    while(num2): # this means as long as num2 is not equal to 0
        print("Before starting")
        print(num1)
        print(num2)
        num1, num2 = num2, num1%num2 # This is called tupple assignment
        print("After %")
        print(num1)
        print(num2)
    return num1 # returning num1 because last non zero remainder is GCD

Gcd = calc_gcd(a,b)
print(f"GCD of {a} and {b} is {Gcd}")    
