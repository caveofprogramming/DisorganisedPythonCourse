#!./venv/bin/python

# RFC 5322 

import re

def main():
    html = r"<div id='greeting'>Hello!</div>"

    result = re.match(r"""
              <(\w{2,10})\s+ # Match opening tag
              [^>]*
              >              # Closing bracket of opening tag
              ([^<>]+)
              </             # Opening bracket of closing tag
              \1
              >              # Closing bracket of closing tag
            """, html, re.VERBOSE)

    if not result is None:
        print("Match: " + ", ".join(result.groups()))
    else:
        print("No match")


main()