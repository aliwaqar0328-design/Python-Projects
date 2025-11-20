"""
        Prime Number Checker
"""
def is_prime(number):
    if number < 2:
        return False
    for i in range(2,number):
        if number%i ==0:
            return False
        
    return True

user_input=int(input("Enter the number : "))
number = user_input
if is_prime(number):
    print(f"{number} is Prime")
else :
    print(f"{number} is not Prime")