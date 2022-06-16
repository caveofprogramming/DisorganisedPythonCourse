#!./venv/bin/python

"""
Print all the cubic numbers up to and including 729
Print all the square numbers up to and including 729

Which cubic numbers are also square numbers?
Which cubic numbers are not square numbers?
"""

def main():
    squares = set([x*x for x in range(28)])
    cubes = set([x*x*x for x in range(10)])

    print(cubes)
    print(squares)

    print(cubes.intersection(squares))
    print(cubes.difference(squares))
    
main()
