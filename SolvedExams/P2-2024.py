import numpy as np
from random import random

def algo_x(p):
    while True:
        Y = int(random()*4)
        U = random()
        if  U < p[Y] / (1.4 * .25):
            return Y

def ejercicio1():
    probabilidades = [.13,.22,.35,.30]
    return algo_x(probabilidades)

def ejercicio2():
    U = random()
    if U < 2/3:
        return (U*1.5)**(1/1.5)
    else:
        return 3*U-1
    
def lamda_t(t):
    if t < 3:
        return 5+5*t
    elif t <= 5:
        return 20
    elif t <= 9:
        return 30 -2*t
    
def hot_dog(T):
    interv = [0,1,2,6,8,9]
    lamda = [5,10,15,18,14,12]
    j = 0
    t = -np.log ( 1 - random() ) / lamda[j]
    Eventos = []
    while t <= T:
        if t <= interv[j]:
            V = random()
            if V < lamda[j]/lamda_t(t):
                Eventos.append(t)
            t += -np.log(1 - random()) / lamda[j]
        else:
            t = interv[j] + (t - interv[j]) * lamda[j] / lamda[j + 1]
            j += 1
    return Eventos

def area(N):
    simulacion = 0
    for _ in range(N):
        x = 3*random()-1.5
        y = 3*random()-1.5
        if x**2 + (y-abs(x)**(3/2))**2 <= 1:
            simulacion += 1
    return 9 * simulacion/N

if __name__ == "__main__":
    print('Ejercicio 1:')
    print(ejercicio1())

    print('Ejercicio 2:')
    estimation = sum(ejercicio2()>1 for _ in range(1000)) / 1000
    print(estimation)

    print('Ejercicio 3:')
    estimation = 0
    for _ in range(1000):
        estimation += len(hot_dog(9))
    estimation /= 1000
    print(estimation)

    print('Ejercicio 4:')
    print(round(area(100000),6))


    