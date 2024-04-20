# Exercise 1a - Practical Exercises 3: Random numbers and Monte Carlo method
from Chapter4 import *

if __name__ == "__main__":
    print("First ten numbers of the von Neumann sequence plus the seed:")
    print()
    for seed in [3792, 1004, 2100, 1234]:
        y = seed
        print(f'Seed: {y}')
        for i in range(10):
            y = vonNeumann(y)
            print(f'y_{i}: {y}')
        print()