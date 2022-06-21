#!./venv/bin/python

def main():
    
    for i in range(1, 11):
        for j in range(1, 11):
            print("{:>4}".format(i*j), end="")
        print()
    
main()
