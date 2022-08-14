#!./venv/bin/python

import matplotlib.pyplot as plt
import numpy as np

def main():

    x = np.linspace(0, 30, 100)
    y = x**2

    plt.figure(figsize=(16,9))
    plt.grid(True)
    plt.title("$y=x^2$")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.plot(x,y, color='red')
    plt.show()

if __name__ == "__main__":  
    main()
