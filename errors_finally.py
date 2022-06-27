#!./venv/bin/python

def main():
    
    try:
        pass
        #raise ZeroDivisionError("Division by zero")
        #raise KeyError("Fake key error!")
    except (ZeroDivisionError, KeyError) as e:
        print(e)
    else:
        print("No exception occurred.")
    finally:
        print("Finally was executed.")
   
    
main()
