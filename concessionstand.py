# Concession Stand Program

# This program outputs a menu for a concession of products and prices
# This programs uses the understanding of dictionaries, lists loop and if elif statements.
# Thanks for visiting 

menu = {

     "jollofRice": 170,
     "friedRice": 230,
     "pap" : 200,
     "akara": 170,
     "Pizza": 300,
     "Burger": 250,
     "Chicken": 340,
     "soda":150
     }


total = 0 # Decalred a variable to hold the total price of items
Choice = [] # List to hold the user's choices

print("Welcome to My Concession Stand")

print("Here is the menu: ")

for key , values in menu.items(): # For loop to iterate throught the menu dictionary and print each item and their coressponding prices
    print(f"{key} ------------------- ${values}") # Print statement


while True: #While loop to continue storing the user's food choice until the user decoides to stop
    Food = input("Enter your choice: ").strip().lower() # Input statemnt to get and store the user's food choice. ,strip() removes spaces and lower() converts input to lowercase

    # if statement to check if the user is done picking
    if Food == "q":
        print ("Thanks for visiting the concession stand")
        break
    elif menu.get(Food) is not None: # else statement that stores the user's choice into a list chosen because it can be easily modified
        Choice.append(Food) 


for Food in Choice:  # For loop to iterate throught the dictionary and get the value of price and add it to total
   total += menu.get(Food)

print(f"Your total is ${total}") 