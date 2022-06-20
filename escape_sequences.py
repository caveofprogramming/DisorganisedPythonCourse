#!./venv/bin/python

def main():
    print("Hello")
    print("Hello number " + str(7))
    print("Hello number ", 7)
    print("banana", 2.3, ["hello", "there"], 4, "cherry")

    print("London".lower())
    print("London".casefold())
    print(", ".join(["dog", "cat", "mouse"]))
    print("Hello there", end=" ")
    print("Hello there")

    print("Hello\nhow\nare\nyou?")
    print("This is a tab")
    print("\tone")
    print("\ttwo")
    print()
    print("What is 4\\3 ?")
    print('"Hi", he said."')
    print("'Hi', he said.")
    print("\"Hi\", he said.")
    
main()
