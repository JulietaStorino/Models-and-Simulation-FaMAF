# Exercise 8a - Practical Exercises 3: Random numbers and Monte Carlo method
from random import random
from math import exp

def CalculateN(Nsim):
    estimation = 0
    for _ in range(Nsim):
        U = random()
        N = 1
        while U > exp(-3):
            U *= random()
            N += 1
        estimation += N
    return estimation/Nsim

if __name__ == "__main__":
    iterations = [100, 1000, 10000, 100000, 1000000]
    for iteration in iterations:
        estimation = CalculateN(iteration)
        print(f'Iterations: {iteration}.')
        print(f'Estimation obtained: {estimation}.\n')