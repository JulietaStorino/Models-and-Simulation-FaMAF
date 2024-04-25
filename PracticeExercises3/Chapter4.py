from random import random

# Estimation of the integral of g in the interval (0,1) with Nsim simulations
def MonteCarlo_0_1(g, Nsim):
    Integral=0
    for _ in range(Nsim):
        Integral += g(random())
    return Integral/Nsim

# Estimation of the integral of g in the interval (a,b) with Nsim simulations
def MonteCarlo_a_b(g, a, b, Nsim):
    Integral=0
    for _ in range(Nsim):
        Integral += g(a + (b-a) * random())
    return Integral*(b-a) / Nsim

# Estimation of the integral of g in the interval (0,inf) with Nsim simulations
def MonteCarlo_0_inf(g, Nsim):
    Integral=0
    for _ in range(Nsim):
        u=random()
        Integral += g(1/u-1) / (u**2)
    return Integral/Nsim

# Estimation of the multiple integral of g in the interval (0,1)^2 with Nsim simulations
def MultipleMonteCarlo_0_1(g, Nsim):
    Integral=0
    for _ in range(Nsim):
        Integral += g(random(),random())
    return Integral/Nsim

# Estimation of the multiple integral of g in the interval (0,inf)x^2 with Nsim simulations
def MultipleMonteCarlo_0_inf(g, Nsim):
    Integral=0
    for _ in range(Nsim):
        u1=random()
        u2=random()
        Integral += g(1/u1-1, 1/u2-1) / ((u1**2)*(u2**2))
    return Integral/Nsim