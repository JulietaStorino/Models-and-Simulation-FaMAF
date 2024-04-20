from random import random

# Monte Carlo function to estimate the integral of g at (0,1)
def g(u):
    # Function to integrate into (0,1)
    return (1 - u ** 2) ** (1.5)


def MonteCarlo(g, Nsim):
    # Estimation of the integral of g with Nsim simulations
    Integral = 0
    for _ in range(Nsim):
        Integral += g(random())
    return Integral/Nsim

# Monte Carlo function to estimate the integral of g in (a,b)
def funciong(x):
    # Function to integrate
    return exp(x ** 2 + x)

def IntegralMonteCarlo(funciong, a, b, Nsim):
    # Estimate the integral of function between a and b with Nsim simulations
    Integral = 0
    for _ in range(Nsim):
        Integral += g(a + (b-a) * random())
    return Integral * (b-a)/Nsim

# Estimating the value of pi with Monte Carlo
def valorPi(Nsim):
    enCirculo = 0.
    for _ in range(Nsim):
        u = 2 * random() -1
        v = 2 * random() - 1
        if u ** 2 + v ** 2 <= 1:
            enCirculo += 1
    return 4 * enCirculo/Nsim
    