import random

print("Enter 0 for snake, 1 for water and 2 for gun.")
user = int(input("Enter a number from the above:\n"))
comp = random.randint(0, 2)


def checkNum(comp, user):
    if (comp == user):
        return 0
    if comp == 0 and user == 1:
        return -1

    if comp == 1 and user == 2:
        return -1

    if comp == 2 and user == 0:
        return -1
    return 1
#-1=user loss, 1= user win, 0= score draw
#it will check the score of both of user and comp
score = checkNum(comp, user)

print("You:", user)
print("Computer: ", comp)
if (score == 0):
    print("Score draw")
elif (score == -1):
    print("You lose")
elif (score == 1):
    print("Congo! you won")
