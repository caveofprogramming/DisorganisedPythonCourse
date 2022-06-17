#!./venv/bin/python

def main():
    fruits = {
        "grape": "green",
        "mango": "yellow",
        "apple": "green",
        "orange": "orange",
        "banana": "yellow",
    }

    fruits.pop("banana")
    del fruits["orange"]

    print("Fruits2: ")
    fruits2 = fruits.copy()
    # or
    fruits2 = dict(fruits)
    print(fruits2)

    fruit = fruits.get("raspberry", "red")
    print(fruit)

    print("Fruits1: ")
    print(fruits)


main()