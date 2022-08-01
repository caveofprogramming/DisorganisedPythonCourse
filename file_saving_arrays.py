#!./venv/bin/python

# array python python.org

from array import array

def main():
    numbers = [1.23, 0.0001, -5.678, 4.01, 512.23, 1.123456789]
    number_values = len(numbers)
    filename = "numbers.dat"

    values = array('f', numbers)

    with open(filename, 'wb') as file:
        values.tofile(file)

    del values

    with open(filename, 'rb') as file:
        values = array('f')
        values.fromfile(file, number_values)

    print(list(values))

if __name__ == "__main__":  
    main()
