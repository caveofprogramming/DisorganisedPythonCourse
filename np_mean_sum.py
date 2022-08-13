#!./venv/bin/python

import numpy as np

def main():
    m = np.arange(12).reshape(3, 4)

    print(m)

    print(m.sum(axis=0))
    print(m.sum(axis=1))
    print(m.mean(axis=0))
    print(m.mean(axis=1))

    print(m.flatten())

    print(np.flip(np.sort(np.array([3, 6, 7, 1, 2]))))

if __name__ == "__main__":  
    main()
