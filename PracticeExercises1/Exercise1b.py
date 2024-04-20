# Exercise 1b - Practical Exercises 3: Random numbers and Monte Carlo method
from Chapter4 import *

if __name__ == "__main__":
    print("First ten numbers of the LCG sequence plus the seed:")
    print()
    for seed in [4, 50]:
        y = seed
        print(f'Seed: {y}')
        for i in range(10):
            y = randMixto(5, 4, 2**5, y)
            print(f'y_{i}: {y}')
        print()