
number = int(input("Enter the number : "))
fact = 1
if number < 0 :
    print(f"The number {number} does not have any factorial")
if number == 0 :
    print("The factorial is 1 ")
if number > 0 :
    for i in range(1, number+1):
        fact = fact * i
    print(f"The factorial of {number} is {fact}")