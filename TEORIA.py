#Funcion que calcula la probabilidad de encontrarlo en una posición en particular.
import math
def mod_cuadrado(c):
    return round(c.real * 2 + c.imag * 2, 2)

def norma(v1):
    ima = 0
    for i in range(len(v1)):
        ima += mod_cuadrado(v1[i])
    ima = math.sqrt(ima.real)
    return ima

def normalizar(v1):
    normal = norma(v1)
    for i in range(len(v1)):
        v1[i] = v1[i]*(1/normal)
    return v1

def probabilidad(posic, v1):
    if posic < len(v1):
        if norma(v1) != 1:
            v1 = normalizar(v1)
        p = mod_cuadrado(v1[posic])
        y = 0
        for i in range(len(v1)):
            y += mod_cuadrado(v1[i])
        return p/y
    else:
        return "La posicion no esta en los limites del vector"

#2. El sistema si se le da otro vector Ket debe buscar la probabilidad de transitar del primer vector al segundo.
def prod_interno(v1, v2):
    if len(v1) == len(v2):
        sum = 0
        for i in range(len(v1)):
            sum  += v1[i].conjugate()*v2[i]
    else: sum = "Tamaño errado"
    return sum

def prob_transi(v1,v2):
    p = prod_interno(v2,v1)
    p = p / (norma(v1)*norma(v2))
    probabili = mod_cuadrado(p)
    return probabili








