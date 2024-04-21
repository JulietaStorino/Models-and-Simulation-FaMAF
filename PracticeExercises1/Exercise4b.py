# Exercise 4b - Practice Exercises 3: Random numbers and Monte Carlo method
from random import random, expovariate
from Exercise4a import simulation

if __name__ == "__main__":
    Probability = 0
    box1, box2, box3 = 0, 0, 0
    for _ in range(1000):
        simulatedBox, simulatedTime = simulation()
        if simulatedBox == 1:
            box1 += 1
        elif simulatedBox == 2:
            box2 += 1
        else:
            box3 += 1
    box1 /= 1000
    box2 /= 1000
    box3 /= 1000
    print('Probability that a customer has chosen')
    print(f'    Box 1: {box1}')
    print(f'    Box 2: {box2}')
    print(f'    Box 3: {box3}')
    
