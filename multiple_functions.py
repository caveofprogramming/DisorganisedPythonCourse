#!./venv/bin/python

def greeting():
    print("Hello again!")

def check_password():
    PASSWORD = "hello123"
    password = input("Enter your password > ")

    if password == PASSWORD:
        print("Access granted.")
    else:
        print("Access denied")

def main():
    greeting()
    check_password()

main()


