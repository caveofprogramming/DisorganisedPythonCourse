#!./venv/bin/python

def printb(value):
    print(f"{value & 0b11111111:08b}")

def main():
    pass

if __name__ == "__main__":  
    num1 = 0b00001000
    num2 = 0b00001001

    printb(num1)
    printb(num2)
    printb(num1 ^ num2)

    print(True != False)

    printb(~num2)
