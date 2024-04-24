from random import random
from math import e

def CalculateN(Nsim):
    estimation = 0
    for _ in range(Nsim):
        U = random()
        N = 1
        while U <= 1:
            U += random()
            N += 1
        estimation += N
    return estimation/Nsim

if __name__ == "__main__":
    print(f'Estimation from math library: {e}.\n')
    iterations = [100, 1000, 10000, 100000, 1000000]
    for iteration in iterations:
        estimation = CalculateN(iteration)
        print(f'Iterations: {iteration}.')
        print(f'Estimation obtained: {estimation}.\n')