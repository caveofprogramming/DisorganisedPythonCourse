#!./venv/bin/python

import re

def main():
    email = "john@caveofprogramming.com"

    result = re.match("(\w+)\@(\w+)\.(\w+)", email)

    if result is not None:
        print(f"Match: {result.group(0)}")

        print(result.group(1))
        print(result.group(2))
        print(result.group(3))

        (name, domain, suffix) = result.groups()

        print(len(result.groups()))

        print(f"{name}, {domain}, {suffix}")
    
main()
