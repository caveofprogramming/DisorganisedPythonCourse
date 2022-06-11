#!./venv/bin/python

def new_patient(name="Unknown", type="Unknown", age=-1):
    print(name + ": " + type + "; " + str(age) + " years old.")

def main():
    new_patient("Biffy", "dog", 5)
    new_patient("Tiddles", "cat", 9)
    new_patient("Rover", "dog")
    new_patient()

main()