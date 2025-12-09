def is_leap_year(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    else:
        return False
    
user_input= int(input("Enter the leap year: "))
if is_leap_year(user_input):
    print(f"The year {user_input} is a leap year")
else:
    print(f"The year {user_input} is not a leap year")