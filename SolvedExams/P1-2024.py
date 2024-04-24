#Resolution of the first partial of 2024
from math import log
from random import random

def g(x):
    return 1/((x+1)**2 * log(x))

def monte_carlo(N):
    Integral = 0
    for _ in range(N):
        u = random()
        Integral += g(1/u-1) / (u**2)
    return Integral/N

def ejercicio3():
    iterations = [1000, 10000, 100000]
    for iteration in iterations:
        Estimation = monte_carlo(iteration)
        print(f'{iteration} iterations: {Estimation}')

if __name__ == "__main__":
    ejercicio3()
