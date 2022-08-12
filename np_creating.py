#!./venv/bin/python

import numpy as np

def main():
    # Zeros
    print(np.zeros(5, dtype=int))

    values = np.zeros([2, 3, 4])
    print(values)
    print(values.ndim)
    print()
    print(np.zeros([2, 3]))

    # ranges
    print(np.arange(2, 8, 0.5))

    # linearly spaced
    print(np.linspace(4, 8, 5))

    # random
    print(np.random.rand(5))

    # random, normally distributed
    print(np.random.randn(5))

    # reshape
    print(np.random.rand(9).reshape(3, 3))
  

if __name__ == "__main__":  
    main()
