#!./venv/bin/python

def main():
    NAME = "Oscar"
    name = "oscar"

    print(NAME.casefold() == name.casefold())

    print(NAME.casefold())

    print("ß".casefold())

    lookup = dict()

    value = lookup.get("lkjlkj")

    print(value)
    print(type(value))

    print(value is None)
    
main()
