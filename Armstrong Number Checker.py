#         
# Armstrong number means if a number is 153
# # It will be armstrong if 1^3 + 5^3 + 3^3 = 153 again
# Note: The power will be decided on basis of how many digits are there in a number..

def arm_strong_num(number):
    str_num = str(number)
    len_num = len(str_num)
    total = sum(int(digit) ** len_num for digit in str_num)
    return number == total

try:
    user_input = int(input("Enter Your number: "))
    if arm_strong_num(user_input):
        print(f"The number {user_input} is an armstrong number.")
    else :
        print(f"The number {user_input} is not a armstrong number.")
except ValueError:
    print("Please type an integer")


