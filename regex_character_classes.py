#!./venv/bin/python

# RFC 5322 

import re

def main():
    email = "üjohn-spam.purcell@caveofprogramming.com"

    result = re.match(r"[üa-z][\w\.\-]{2,29}@\w{2,40}\.\w{2,10}", email)

    print("No match" if result is None else "Match")


main()