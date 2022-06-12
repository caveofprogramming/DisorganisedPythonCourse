#!./venv/bin/python

def main():
    fruits1 = ("apple", "orange")
    fruits2 = ("pineapple", "pear")

    animals1 = ["lion", "giraffe"]
    animals2 = ["goat", "dog"]

    number = 3
    number += 2

    print(number)

    print(id(fruits1))
    fruits1 += fruits2
    print(id(fruits1))
    print(fruits1)

    print(id(animals1))
    animals1 += animals2
    print(id(animals1))
    print(animals1)

main()
