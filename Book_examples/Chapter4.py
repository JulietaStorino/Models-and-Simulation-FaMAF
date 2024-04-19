# Secuencia de Von Neumann
def vonNeumann(u):
    u = ((u**2 // 100) % 10000)
    return u

# Generador congruencial lineal mixto
def randMixto(a,c,M,u):
    return (a*u+c) % M 

# Generador congruencial lineal multiplicativo
def randMulti(a,M,u):
    return (a*u) % M
