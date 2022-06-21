#!./venv/bin/python

import re

def main():

    """
    \w  alphanumeric
    \d  number
    \s  space
    .   any character

    *   zero or more of the preceeding symbol, greedy match
    +   one or more of the preceeding symbol
    *?   zero or more of the preceeding symbol, non-greedy match
    """

    text = "The temperature is: 31"
    result = re.match(".*\:\s*(\d+)", text)
    print("No match" if result is None else f"Match: {result.group(1)}")

    
main()
