# Exercise 1 - Practical Exercises 3: Random numbers and Monte Carlo method
from random import randrange

def find_period_linear_generator(a,c,M):
    ''' 
    Given a, c, M, variables that define the linear
    generator y_{i+1}=ay_i+c mod (M) returns the period
    of the sequence
    '''
    seed = randrange(M) #y_0
    period = 1
    y = (a * seed + c) % M #y_1
    while not y == seed:
        y = (a * y + c) % M
        period += 1
    return (seed, period)

def is_maximum_period(c,M,period):
    return (period == M) or (period == M-1 and c == 0)

if __name__ == "__main__":
    values = ((125,3,2**9),(123,3,2**9),(5,0,71),(7,0,71))
    for value in values:
        a,c,M = value
        data = find_period_linear_generator(a,c,M)
        seed,period = data
        print(f'Case: a = {a}, c = {c}, M = {M}.')
        print(f'    Seed: {seed}, period: {period}.')
        if is_maximum_period(c,M,period):
            print('    Got the maximum period.')
        else:
            print('    Did not get maximum period.')
        print()
