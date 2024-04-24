# Exercise 8b - Practical Exercises 3: Random numbers and Monte Carlo method
from random import random
from math import exp

def CalculateProbabilityN(i):
    estimation = 0
    for _ in range(1000000):
        U = random()
        N = 1
        while U > exp(-3):
            U *= random()
            N += 1
        if N == i:
            estimation += 1
    return estimation/1000000

if __name__ == "__main__":
    for i in range(7):
        estimation = CalculateProbabilityN(i)
        print(f'P(N={i}) = {estimation}')