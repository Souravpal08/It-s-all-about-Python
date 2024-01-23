import random
User_choice=int(input("Please choice a number: 0 for rock, 1 for Paper & 2 for scissors "))
if User_choice >=3 & User_choice <0:
    print("You have entered invalid number. Please select a valid number.")
else:
 computer_choice=random.randint(0,2)
print(f"Computer chose:{computer_choice}")
if computer_choice == User_choice:
    print("It's draw!")
elif computer_choice == 0 & User_choice == 2:
    print("You lose..!")
elif computer_choice == 2 & User_choice == 0:
    print("You won..!")
elif computer_choice > User_choice:
    print("You lose..!")
elif computer_choice< User_choice:
    print("You won..!")
play_again=input("Want to play again?(Yes/No)")

if play_again.lower() !='yes':
     breakpoint()

