#!./venv/bin/python

import matplotlib.pyplot as plt
import numpy as np

def main():
    x = np.random.randn(10000)

    plt.hist(x, bins=20, edgecolor="white")
    plt.show()

if __name__ == "__main__":  
    main()
