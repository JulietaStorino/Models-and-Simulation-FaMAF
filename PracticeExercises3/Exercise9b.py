# Exercise 9b - Practical Exercises 3: Random numbers and Monte Carlo method
from random import randint

def simulation():
    U = randint(1, 6)
    if U == 1 or U == 6:
        score = randint(1, 6)*2
    else:
        score = randint(1, 6) + randint(1, 6)
    return score > 6

if __name__ == "__main__":
    estimation = 0
    for _ in range(1000000):
        estimation += simulation()
    estimation /= 1000000
    print(f'Probability of winning the game: {estimation}')