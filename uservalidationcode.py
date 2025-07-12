# This code validates user input and stores
# User name requirements: 
# -Username should not exceed more than 12 characters
# -Must not contain spaces
# -Must not contain digits

print("Welcome to the username validation")
print("Username reuirements: ")
print("Must not exceed more than 12 characters, Must not contain spaces, Must not contain digits")

username = input("Enter your username: ").strip()

loo = True

while loo: # While loop to continue looping until a valid username has been enteres
    if len(username) > 12:  # If statement to check is username is below 12 characters
        print("Username is length is exceed required lenght.")
        username = input("Enter new your username: ").strip()
       
    elif not username.isalpha():
        print("Username must not contain digits or spaces.")
        username = input("Enter new your username: ").strip()

    elif username.count(" ") > 0:
        print("Username must not contain spaces.")
        username = input("Enter new your username: ").strip()
    else:
     print("Username requirements have been met.")
     print(f"You are welcome {username}")
     loo = False
     
    

       
