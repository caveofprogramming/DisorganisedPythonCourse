#!./venv/bin/python

def greeting():
    print("Hello!")
    response = input("Are you OK? y/n > ")

    if(response == "y"):
        print("Good to hear.")
    else:
        print("Sorry to hear you are not OK.")

greeting()