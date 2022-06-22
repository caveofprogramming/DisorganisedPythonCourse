#!./venv/bin/python

# RFC 5322 

import re

def main():
    html = r'<span id="greeting">Hello!</span>'

    result = re.match(r"<span\s+[^>]*id\=\"(\w+)\"[^>]*>", html)

    if not result is None:
        print(f"Match: {result.group(1)}")


main()