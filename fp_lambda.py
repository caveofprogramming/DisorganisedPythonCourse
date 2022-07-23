#!./venv/bin/python

def main():
    animals = ['cat', 'Dog', 'giraffe', 'Badger']
    animals = map(lambda str: str.lower(), animals)

    print(list(animals))

if __name__ == "__main__":  
    main()
