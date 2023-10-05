#Funcion que calcula la probabilidad de encontrarlo en una posición en particular.
import Lib2matrces as lib
import math
import numpy as np
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

#RETOS DE PROGRAMACIÓN DEL CAPÍTULO 4.
def media(mat, ket):
    if norma(ket) != 1:
        ket = normalizar(ket)
    resp = lib.hermitiana(mat)
    if resp == "NO es hermitiana" or resp == "Tamaño de matriz incorrecto":
        return resp
    else:
        final = lib.prod_interno(lib.sobrevector(mat, ket), ket)
        return final.real

def varianza(mat, ket):
    if norma(ket) != 1:
        ket = normalizar(ket)
    resp = lib.hermitiana(mat)
    if resp == "NO es hermitiana" or resp == "Tamaño de matriz incorrecto":
        return resp
    else:
        identidad = [[0 for i in range(len(mat))] for j in range(len(mat))]
        for i in range(len(identidad)):
            for j in range(len(identidad)):
                if i == j:
                    identidad[i][j] = 1
        operador = lib.multi_escalar_matriz(media(mat, ket), lib.inversamatriz(identidad))
        delta = lib.sumatriz(mat, operador)
        cuadrado = lib.prod_de_matz(delta,delta)
        return media(cuadrado,ket)

def val_prop(mat):
    mat = np.array(mat)
    valores = np.linalg.eigvals(mat)
    return valores

def vect_prop(mat):
    mat = np.array(mat)
    valores, vectores = np.linalg.eig(mat)
    return vectores

def transitar_vect_prop(mat, ket):
    if norma(ket) != 1:
        ket = normalizar(ket)
    vectores = vect_prop(mat)
    prob = []
    for i in range(len(vectores)):
        proba = prob_transi(ket,vectores[i])
        prob.append(proba)
    return prob

def final(seq, ket):
    estado = ket
    chack = True
    for i in range(len(seq)):
        unit = lib.unitario(seq[i])
        if unit == "NO es unit" or unit == "Tamaño de matriz incorrecto":
            chack = False
            break
    if chack:
        for i in range(len(seq)):
            estado = lib.sobrevector(seq[i],estado)
        return estado
    else:
        return "No son unitarias algunas de las matrices."






