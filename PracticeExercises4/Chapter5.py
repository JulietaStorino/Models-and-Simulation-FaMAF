from random import random

''''
 Método de la transformada inversa para generar v.a. discretas
    - x: vector de valores posibles de X (ordenados)
    - p: vector de probabilidades (ordenados)
'''
def Metodo_transformada_inversa(p, x):
    U=random()
    i=0; F=p[i]
    while U >= F:
        i += 1; F += p[i]
    return x[i]

''''
 Método de la transformada inversa para generar una v.a.
 uniforme discreta de 1 a n
'''
def Metodo_transformada_inversa_uniforme(n):
    return int(n*random()) + 1

''''
 Método de la transformada inversa para generar una v.a.
 uniforme discreta en el intervalo {m,k}
'''
def Metodo_transformada_inversa_uniforme_m_k(m,k):
    return int(random()*(k-m+1)) + m

'''
 Ejemplos de aplicaciones de la generación de v.a. uniformes discretas
'''
def permutación_aleatoria(a):
    N = len(a)
    for j in range(N-1):
        indice = Metodo_transformada_inversa_uniforme_m_k(j, N-1)
        a[j], a[indice] = a[indice], a[j]
    return a

def permutación_aleatoria_mejorada(a):
    N = len(a)
    for j in range(N-1,0,-1):
        indice = Metodo_transformada_inversa_uniforme(j+1)
        a[j], a[indice] = a[indice], a[j]
    return a

def combinación_aleatoria_n_m(r,A):
    N = len(A)
    for j in range(N-1, N-1-r, -1):
        indice = Metodo_transformada_inversa_uniforme_m_k(j, N-1)
        A[j], A[indice] = A[indice], A[j]
    return A[N-r:]

