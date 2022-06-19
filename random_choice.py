#!./venv/bin/python

import random

def main():
    fruits = ("banana", "apple", "raspberry", "mango")

    fruit = random.choice(fruits)
    
    print(fruit)

main()