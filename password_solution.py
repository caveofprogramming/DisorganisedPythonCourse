#!./venv/bin/python

"""

Write a program that asks the user to enter a password and compares it to a hard-coded password.

If the password is correct, the program prints "Greetings Professor Falcon" and exits.

If the password is incorrect, the program prints "Access denied" and then asks for the password again.

The program will ask for the password three times if necessary.

After that, it exits.

"""

PASSWORD = "hello123"


for i in range(0, 3):
    password = input("Enter your password > ")

    if(password == PASSWORD):
        print("Greetings Professor Falcon")
        break
    else:
        print("Access denied")

