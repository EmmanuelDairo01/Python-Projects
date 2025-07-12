# This a weigh calculator program using Python
# It asks the user for their weight 
# And the the unit of weight measurement either pounds or kilograms
# It then converts the weight if pounds converts to kilograms and if kilograms converts to pounds
# It does not involve a while loop
# This is a simple program to demostratr the use of if - elif - else statements

print("Welcome to the weight calculator program")

weight = float(input("Enter your weight: ")) # Ask user for weight value and store it into weight
units = input("Enter the unit of weight either pounds or kilograms: ").strip().lower() # ask the user for unit of weight measurement

if units == "pounds": # If statment to chck if units is pounds
    convert = weight * 0.453592
    print(f"Yor weight in kilograms is {convert:.2f} kg")
elif units == "kilograms" : # If statement to check if units is in kilograms
    convert = weight / 0.453592
    print(f"Your weight in pounds is {convert:.2f} lbd")
else :
    print("Invalid weight mesurement unit.") # Message to display to the user that an invalid unit of measurement was enetered
    while units.lower() not in ["pounds" , "kilograms"]: # While loop to continue asking the user for valid unit until a valid unit is entered which is either pounds or kilograms
        print("Please enter a valid weight meauremnt. ")
        units = input("Enter the unit of weight either pounds or kilograms: ").strip().lower()
        if units == "pounds":
          convert = weight * 0.453592
          print(f"Yor weight in kilograms is {convert:.2f} kg")
        elif units == "kilograms" :
          convert = weight / 0.453592
          print(f"Your weight in pounds is {convert:.2f} lbd")


