#!./venv/bin/python

def main():
    numbers = {1, 2, 3} 
    print(numbers)

    number_list = [1, 2, 3, 1, 2, 4]
    print(number_list)

    no_duplicates = set(number_list)

    print(no_duplicates)

    for x in no_duplicates:
        print(x)
    
    print(3 in no_duplicates)

main()
