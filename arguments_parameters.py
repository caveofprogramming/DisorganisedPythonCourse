#!./venv/bin/python

def greet(user):
    print("Hello " + user)

def main():
    name = input("What's your name? > ")
    greet(name)

main()

