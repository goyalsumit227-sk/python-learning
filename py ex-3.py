password = "python123"

user_input = input("Enter the password: ")

while user_input != password:
    print("Incorrect password. Please try again.")
    user_input = input("Enter the password: ")

print("Access granted!")
