#!./venv/bin/python

def main():

    fruits = ["apple", "cherry", "orange"]
    print(fruits)

    fruits.append("banana")
    fruits.append("pineapple")
    print(fruits)

    fruits[1] = "raspberry"
    print(fruits)

    fruits[2:4] = ["blackberry", "melon", "grape"]
    print(fruits)
    return


main()
