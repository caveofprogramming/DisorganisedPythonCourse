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

    category_totals = dict()
    day_totals = dict()

    for line in lines:

        if not re.search(r"\S", line):
            continue

        fields = re.split(r"\s+", line)

        if headings is None:
            headings = fields

            for k in range(1, len(headings)):
                category_totals[headings[k]] = 0
            continue

        day = fields[0]
        day_totals[day] = 0

        for i in range(1, len(fields)):
            category = headings[i]
            value = float(fields[i])
            category_totals[category] += value
            day_totals[day] += value
        
    print(category_totals)
    print(day_totals)
    
main()
