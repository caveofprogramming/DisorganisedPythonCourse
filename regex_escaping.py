#!./venv/bin/python

import re

def main():
    text = r"--al_ke\n--k"

    print(text)

    print(re.match(r"[a-z\-_]*\\n.*", text))
    
main()
