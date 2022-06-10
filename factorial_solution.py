#!./venv/bin/python

"""
Write a function that calculates the factorial of a number.

The factorial of a number is defined like this:

n! = n * (n - 1) (n - 2) * ... * 3 * 2 * 1

e.g. 

3! = 3 * 2 * 1
5! = 5 * 4 * 3 * 2 * 1

abo
aob
bao
boa
oba
oab

The factorial of zero, 0!, is defined as 1.

Calcuate the factorial of 7 , i.e. 7!
"""

def factorial(number):
    value = 1

    for n in range(1, number + 1):
        value = value * n

    return value

def main():

    print(factorial(3))
    print(factorial(0))
    print(factorial(7))
    
main()
