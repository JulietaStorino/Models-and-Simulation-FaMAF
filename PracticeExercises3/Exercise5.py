# Exercise 5 a..f - Practical Exercises 3: Random numbers and Monte Carlo method
from random import random
import numpy as np
import Chapter4 as ch

def a(x):
    return (1 - x**2) ** (3/2) 

def b(x):
    return x / (x** 2 - 1)

def c(x):
    return x * (1 + x**2)**(-2)

def d(x):
    return 2 * np.exp(-x**2)

def e(x,y):
    return np.exp((x+y)**2)

def I(y,x): #I_y(x)
    return y < x

def f(x,y):
    return np.exp(-(x+y)) * I(y,x)

if __name__ == "__main__":
    iterations = [100, 1000, 10000, 100000, 1000000]
    print('Estimations:\n')
    #5a
    print(f'\ta:')
    for iteration in iterations:
        Estimation = ch.MonteCarlo_0_1(a, iteration)
        print(f'\t\t {iteration} iterations: {Estimation}')
    #5b
    print(f'\tb:')
    for iteration in iterations:
        Estimation = ch.MonteCarlo_a_b(b, 2, 3, iteration)
        print(f'\t\t {iteration} iterations: {Estimation}')
    #5c
    print(f'\tc:')
    for iteration in iterations:
        Estimation = ch.MonteCarlo_0_inf(c, iteration)
        print(f'\t\t {iteration} iterations: {Estimation}')
    #5d
    print(f'\td:')
    for iteration in iterations:
        Estimation = ch.MonteCarlo_0_inf(d, iteration)
        print(f'\t\t {iteration} iterations: {Estimation}')
    #5e
    print(f'\te:')
    for iteration in iterations:
        Estimation = ch.MultipleMonteCarlo_0_1(e, iteration)
        print(f'\t\t {iteration} iterations: {Estimation}')
    #5f
    print(f'\tf:')
    for iteration in iterations:
        Estimation = ch.MultipleMonteCarlo_0_inf(f, iteration)
        print(f'\t\t {iteration} iterations: {Estimation}')
