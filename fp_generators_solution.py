#!./venv/bin/python

def main():
    print(list(x for x in range(0, 3)))
    print(set(x for x in range(0, 3) if x != 1))
    print(tuple('*' if x == 0 else x for x in range(0, 3)))
    print(tuple('*' if x == 0 else x for x in range(0, 3) if x != 1))

if __name__ == "__main__":  
    main()
