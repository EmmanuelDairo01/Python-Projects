import random


def rool_dice():
    return random.randint(1,6)

print("Welcome to the dice rolling game! \n")

print("Roll a dice and see what you get! \n")

print("Press y to start generate value for dice") 

num = int(rool_dice())

print("You rolled a", num)

answer = input("Press y to roll again or any othe key to exit").strip().lower()

while answer == "y":
    num = rool_dice()
    print("You rolled a", num)
    answer = input("Press y to roll again or any other key to exit").strip().lower()
else:
    print("Thanks for playing! Thanks for playing!")
