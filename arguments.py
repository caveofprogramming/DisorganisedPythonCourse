#!./venv/bin/python

def greet(name):
    print("Hello " + name)

def main():

    name = input("What's your name? > ")
    greet(name)

main()