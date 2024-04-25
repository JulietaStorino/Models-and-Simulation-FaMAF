# Von Neumann sequence
def vonNeumann(u):
    u = ((u**2 // 100) % 10000)
    return u

# Mixed Linear Congruent Generator with multiplier a, increment c and modulus M
def randMixto(a,c,M,u):
    return (a*u+c) % M 

# Multiplicative Linear Congruent Generator with multiplier a and modulus M
def randMulti(a,M,u):
    return (a*u) % M
