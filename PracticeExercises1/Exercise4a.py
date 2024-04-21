# Exercise 4a - Practice Exercises 3: Random numbers and Monte Carlo method
from random import random, expovariate

def simulation():
    U = random()
    if U < .40:
        Box = 1
        waitingTime = expovariate(1/3)
    elif U < .72:
        Box = 2
        waitingTime = expovariate(1/4)
    else:
        Box = 3
        waitingTime = expovariate(1/5)
    return (Box,waitingTime)

if __name__ == "__main__":
    Probability = 0
    for _ in range(1000):
        simulatedBox, simulatedTime = simulation()
        if simulatedTime < 4.0:
            Probability += 1
    simulatedTime /= 1000
    print(f'Probability that a customer waits less than 4 minutes to be served:\n {simulatedTime}')
    
