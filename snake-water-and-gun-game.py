import random

player= input("give your value either snake,water or gun: ")
choices = ["snake","water","gun"]
computer= random.choice(choices)
print(computer)
if (computer == player):
    print("its a draw")
elif (player =="snake" and computer=="water" or player=="water" and computer=="gun" or player =="gun" and computer=="snake"):
    print("player is the winner")
else:
    print("computer is the winner")
