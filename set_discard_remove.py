#!./venv/bin/python

def main():
    numbers = set([x for x in range(0, 15)])

    numbers.remove(3)
    numbers.remove(11)

    print(numbers)

    numbers.discard(100)
    numbers.discard(2)

    print(numbers)
    
main()
