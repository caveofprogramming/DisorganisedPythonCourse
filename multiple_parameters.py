#!./venv/bin/python

def greet(name, is_professor):
    if(is_professor):
        print("Greetings Professor " + name)
    else:
        print("Hello " + name)

def main():
    greet("John", False)
    greet("Sasha", True)

main();