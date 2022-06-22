#!./venv/bin/python

# RFC 5322 

import re

def main():
    html = r"<span id='greeting'>Hello!</span>"

    result = re.match(r"""
            <span\s+    # Match <span followed by at least one space
            [^>]*       # Match any number of anything that isn't ">"
            id\=["'](\w+)["']   # Extract the ID
            [^>]*   # Match any number of anything that isn't ">"
            >       # Match closing ">" of the opening <span> tag
            ([^<]*)
            </span>           
            """, html, re.VERBOSE)

    if not result is None:
        print(f"Match: {result.group(1)}")
        print(f"Match: {result.group(2)}")
    else:
        print("No match")


main()