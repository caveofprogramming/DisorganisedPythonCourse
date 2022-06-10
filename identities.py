#!./venv/bin/python

def greet(user):
    print("Hello " + user)
    print("in greet: " + str(id(user)))

def main():
    name = "John"

    print("in main: " + str(id(name)))
    greet(name)

main()