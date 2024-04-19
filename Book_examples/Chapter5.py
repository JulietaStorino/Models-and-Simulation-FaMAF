from random import random

# Funcion de Monte Carlo para estimar la integral de g en (0,1)
def g(u):
    # Funcion a integrar en (0,1)
    return (1 - u ** 2) ** (1.5)


def MonteCarlo(g, Nsim):
    # Estimacion de la integral de g con Nsim simulaciones
    Integral = 0
    for _ in range(Nsim):
        Integral += g(random())
    return Integral/Nsim

# Funcion de Monte Carlo para estimar la integral de g en (a,b)
def funciong(x):
    # Funcion a integrar
    return exp(x ** 2 + x)

def IntegralMonteCarlo(funciong, a, b, Nsim):
    # Estima la integral de funciong entre a y b con Nsim simulaciones
    Integral = 0
    for _ in range(Nsim):
        Integral += g(a + (b-a) * random())
    return Integral * (b-a)/Nsim

# Estimación del valor de pi con Monte Carlo
def valorPi(Nsim):
    enCirculo = 0.
    for _ in range(Nsim):
        u = 2 * random() -1
        v = 2 * random() - 1
        if u ** 2 + v ** 2 <= 1:
            enCirculo += 1
    return 4 * enCirculo/Nsim
    