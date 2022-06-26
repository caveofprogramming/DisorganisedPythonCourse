#!./venv/bin/python

def do_greet():
    #raise KeyError()
    raise Exception()
    greet()

def greet():
    print("Hello")
    print(1/0)

def main():

    try:
        do_greet()
    except ZeroDivisionError:
        print("Tried to divide by zero!")
    except KeyError:
        print("A key error occured")
    except:
        print("Some unknown error occurred")
    
    
main()
