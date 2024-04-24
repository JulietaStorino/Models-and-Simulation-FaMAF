from random import random, choice
from math import sqrt, pi

def CalculatePi(Nsim):
    estimation = 0
    for _ in range(Nsim):
        x = choice([-1, 1]) * random()
        y = choice([-1, 1]) * random()
        if sqrt(x**2 + y**2) < 1:
            estimation += 1
    return estimation * 4 / Nsim

if __name__ == "__main__":
    print(f'Estimation from math library: {pi}.\n')
    iterations = [1000, 10000, 100000]
    for iteration in iterations:
        estimation = CalculatePi(iteration)
        print(f'Iterations: {iteration}.')
        print(f'Estimation obtained: {estimation}.')
