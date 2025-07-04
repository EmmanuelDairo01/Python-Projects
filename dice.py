"""""
Welcome to my first python project!
This is just a simple dice rolling game 
where you can roll a dice and get a random number between 1 and 6
I know it's simple bit it's a start!
More cool projects coming soon!
Enjoy!
"""


import random # Calls random module to generate random number and choices 

def rool_dice(): # Function to roll a dice
    return random.randint(1,6)

print("Welcome to the dice rolling game! \n") # Prints welcome message

print("Roll a dice and see what you get! \n")

print("Press y to start generate value for dice") # Print message to start rolling the dice

num = int(rool_dice())

print("You rolled a", num) # Prints the value of the dice rolled

answer = input("Press y to roll again or any othe key to exit").strip().lower()

while answer == "y": # While loop to keep rolling the dice if user wants to continue
    num = rool_dice()
    print("You rolled a", num)
    answer = input("Press y to roll again or any other key to exit").strip().lower()
else:
    print("Thanks for playing! Thanks for playing!") # Prints thank you message for playing
