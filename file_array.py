#!./venv/bin/python

# array python python.org

from array import array

def main():
    numbers = [1.23, 0.0001, -5.678, 4.01, 512.23]

    values = array('f', numbers)

    print(values.tolist())

    print(f"{9.999999747378752e-05: f}")

if __name__ == "__main__":  
    main()
