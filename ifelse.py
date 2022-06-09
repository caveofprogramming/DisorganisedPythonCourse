#!./venv/bin/python

NAME = "John"

name = input("Enter your name: ")

if name == NAME:
    print("Name is John")
    print("Name was correct")
else:
    print("Name was incorrect")

print("Bye")