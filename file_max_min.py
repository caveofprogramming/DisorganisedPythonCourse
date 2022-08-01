#!./venv/bin/python

"""
000 0
001 1
010 2
011 3
100 4
101 5
110 6
111 7
"""

def main():
    print(pow(2, 3) - 1)
    print(pow(2, 2) - 1)

    print(pow(2, 8) - 1)
    print(pow(2, 7) - 1)

    print(pow(2, 16) - 1)
    print(pow(2, 15) - 1)

    # 123.456

    # 4 bytes : 7 after the decimal point
    # 8 bytes : 15 digits after the decimal point

if __name__ == "__main__":  
    main()
