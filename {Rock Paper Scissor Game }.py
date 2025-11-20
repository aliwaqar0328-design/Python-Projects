import random

items_list = ["Rock", "Paper", "Scissor"]
users_choice = input("Enter Your Choice : Rock , Paper , Scissor ? ")
comp_choice = random.choice(items_list)
print(f"User Choice : {users_choice}, Computer Choice : {comp_choice}")

if users_choice == comp_choice:
    print("Both Same So, Match Tie !!!")
elif users_choice == "Rock":
    if comp_choice == "Paper":
        print("Paper covers Rock = Computer Wins")
    else:
        print("Rock Smashes Scissor = You Win")
elif users_choice == "Paper":
    if comp_choice == "Rock":
        print("Paper Covers Rock = You Win")
    else:
        print("Scissor Cuts Paper = Computer Wins")
elif users_choice == "Scissor":
    if comp_choice == "Rock" :
        print("Rock Smashes Scissor = Computer Wins")
    else:
        print("Scissor cuts Paper = You Win")
print("GAME OVER")