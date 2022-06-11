#!./venv/bin/python

def describe_ufo(**attributes):
    
    for key in attributes:
        print(key + ": " + attributes[key])


def main():
    describe_ufo(speed="very fast", color="blue", size="huge")
    
main()
