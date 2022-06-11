#!./venv/bin/python

"""
Exercise: define a single function that accepts:
    one or more positional arguments
    zero or more variable arguments
    zero or more variable keyword arguments

    Make the function print out all arguments it receives.
"""

def test(name, *args, **kwargs):
    print(name)
    print()

    for arg in args:
        print(arg)

    for key in kwargs:
        print(key + ": " + str(kwargs[key]))

def main():
    test("Tree", 1, 3, "one", cat="animal", stone="mineral", value=7.3)
    
main()
