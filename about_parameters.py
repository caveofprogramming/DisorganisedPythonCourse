#!./venv/bin/python

def greet(user):
    print("Hello " + user)
    user = "Orange"
    print("user in greet: " + user)

def main():
    name = "John"
    greet(name)
    print("name in main: " + name)

main()