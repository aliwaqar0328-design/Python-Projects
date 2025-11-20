def is_palindrome(astring):
    astring = astring.lower()
    reversed_st = astring[:: -1]
    if astring == reversed_st :
        return True
    else:
        return False
    
user_input=input("Enter Your String : ")
if is_palindrome(user_input):
    print(f"{user_input} is palindrome ")
else:
    print(f"{user_input} is not palindrome")


