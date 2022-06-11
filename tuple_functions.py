#!./venv/bin/python

def main():

    numbers1 = 1, 2, 3, 4, 3, 2

    value1 = numbers1.index(2)
    print(value1)

    value2 = numbers1.count(3)
    print(value2)

    value3 = max(numbers1)
    print(value3)

    numbers2 = 10, 20, 30
    numbers3 = numbers1 + numbers2

    print(numbers3)

    numbers4 = 4 * numbers2
    print(numbers4) 
    return
    
main()
