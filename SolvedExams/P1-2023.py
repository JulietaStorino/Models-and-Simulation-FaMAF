#Resolution of the first partial of 2023
import math
import numpy as np
from random import random

def ejercicio2():
    U = random() 
    V = random()
    gameRound = 1
    playing = True
    while playing:
        if U > .5 and V < .5:
            playing = False
            AWinner = True
        elif U < .5 and V > .5:
            playing = False
            AWinner = False
        else:
            U = random() 
            V = random()
            gameRound += 1
    return (AWinner, gameRound)

def a(x):
    return (x / (x - np.exp(x)))

def b(x):
    return (x**3 * np.exp(-x**3))

# Integral Monte Carlo en el intervalo (a,b)
def MonteCarlo_a_b(f, a, b, Nsim):
    Integral = 0
    for _ in range(Nsim):
        Integral += f(a + (b-a) * random())
    return Integral * (b-a)/Nsim

# Integral Monte Carlo en el intervalo (0,inf)
def MonteCarlo_0_inf(fun, Nsim):
    Integral=0
    for _ in range(Nsim):
        u=random()
        Integral+= fun(1/u-1)/(u**2)
    return Integral/Nsim

def ejercicio4():
    print('    Integral a:')
    for iteration in iterations:
        estimation = MonteCarlo_a_b(a, -3, 3, iteration)
        estimation = round(estimation, 4)
        print(f'        Iteraciones: {iteration}')
        print(f'        Estimación: {estimation}\n')
    print('    Integral b:')
    for iteration in iterations:
        estimation = MonteCarlo_a_b(b, -1, 1, iteration)
        estimation += MonteCarlo_0_inf(b, iteration)
        estimation = round(estimation, 4)
        print(f'        Iteraciones: {iteration}')
        print(f'        Estimación: {estimation}\n')


if __name__ == "__main__":
    iterations = (1000,10000,100000,1000000)
    print('Ejercicio 2:')
    for iteration in iterations:
        estimation = 0
        for _ in range(iteration):
            Awinner, gameRound = ejercicio2()
            if Awinner and (gameRound == 1 or gameRound == 2):
                estimation += 1 
        estimation /= iteration
        print(f'    Iteraciones: {iteration}')
        print(f'    Estimación: {estimation}\n')
    print('Ejercicio 4:')
    ejercicio4()



