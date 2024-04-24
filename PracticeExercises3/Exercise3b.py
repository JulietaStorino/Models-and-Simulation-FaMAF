# Exercise 3b - Practice Exercises 3: Random numbers and Monte Carlo method
from random import random

def simulation(): # 1 Win the game - 0 Fail the game 
    if random() < 1/3:
        X = random()+random()
    else:
        X = random()+random()+random()
    return X<=2

if __name__ == "__main__":
    nvalues = (100,1000,10000,100000,1000000)
    for n in nvalues:
        estimation = 0
        for _ in range(n):
            estimation += simulation()
        estimation /= n
        print(f'Case: n = {n}. P[X<=2] ≈ {estimation}.')