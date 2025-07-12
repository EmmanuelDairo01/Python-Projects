# This a weigh calculator program using Python
# It asks the user for their weight 
# And the the unit of weight measurement either pounds or kilograms
# It then converts the weight if pounds converts to kilograms and if kilograms converts to pounds


weight = float(input("Enter your weight: "))
units = input("Enter the unit of weight either pounds or kilohrams: ").strip().lower()

if units == "pounds":
    convert = weight * 0.453592
    print(f"Yor weight in kilograms is {convert} kg")
elif units == "kilograms" :
    convert = weight / 0.453592
    print(f"Your weight in pounds is {convert} lbd")
else :
    print("Invalid weight mesurement unit.")