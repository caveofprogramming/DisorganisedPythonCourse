#!./venv/bin/python

import re

def main():
    email = "cave.john.w.purcell@caveofprogramming.com"

    result = re.match("(?:\w+\.)*(\w+)", email)

    if result is None:
        print("No match")
    else:
        print(result.groups())
        print(result.group())



main()