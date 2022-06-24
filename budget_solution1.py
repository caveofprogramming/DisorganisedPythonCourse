#!./venv/bin/python

import re

data = """
Day         Electricity     Coffee      Cleaning
Monday      330             10          50
Tuesday     220             12          40
Wednesday   130             14          80
"""

def main():
    lines = re.split(r"[\n\r\f]+", data)

    headings = None

    for line in lines:

        if not re.search(r"\S", line):
            continue

        fields = re.split(r"\s+", line)

        if headings is None:
            headings = fields
            continue

        print(fields)

    
    print(headings)
    
main()
