import math
import numpy

def sumavec(v1, v2):
    c=[]
    if len(v1) == len(v2):
        for i in range(len(v1)):
           c.append(v1[i]+v2[i])
    else:
        c ="Vectores con tamaño diferente"
    return c

def inverso(v1):
    vector = []
    for k in range(len(v1)):
        vector.append(-1*v1[k])
    return vector

def multliescalar(k,v1):
    vector = []
    for i in range(len(v1)):
        vector.append(k * v1[i])
    return vector

def sumatriz(m1,m2):
    fil_a = len(m1)
    fil_b = len(m2)
    col_a = len(m1[0])
    col_b = len(m2[0])
    matriz = []
    if fil_a == fil_b and col_a == col_b:
        for i in range(fil_a):
            fila = []
            for j in range(col_a):
                fila.append(m1[i][j] + m2[i][j])
            matriz.append(fila)
    else:
        matriz = "Tamaños de matrices diferentes"
    return matriz

def inversamatriz(m1):
    fila = len(m1)
    colum = len(m1[0])
    for i in range(fila):
        for j in range(colum):
            m1[i][j] = (-1)*(m1[i][j])
    return m1

def multi_escalar_matriz(k,m1):
    fila = len(m1)
    colum = len(m1[0])
    for i in range(fila):
        for j in range(colum):
            m1[i][j] = k *m1[i][j]
    return m1

def transpuesta(m1):
    fila = len(m1)
    colum = len(m1[0])
    matriz = [[0 for i in range (fila)] for j in range (colum)]
    for i in range(fila):
        for j in range(colum):
            matriz[j][i] = m1[i][j]
    return matriz

def conjugada(m1):
    fila = len(m1)
    colum = len(m1[0])
    for i in range(fila):
        for j in range(colum):
            m1[i][j] = m1[i][j].conjugate()
    return m1

def adjunta(m1):
    m1 = transpuesta(m1)
    m1 = conjugada(m1)
    return m1

def prod_de_matz(m1, m2):
    fl_a = len(m1)
    cl_a = len(m1[0])
    fl_b = len(m2)
    cl_b = len(m2[0])
    if cl_a == fl_b:
        matriz = []
        for i in range(cl_b):
            fila = []
            for i in range(fl_a):
                sum = 0
                for j in range(cl_a):
                    sum += m1[i][j] * m2[j][i]
                fila.append(sum)
            matriz.append(fila)
    else:
        matriz = "Tamaño errado"
    return matriz

def prod_interno(v1, v2):
    if len(v1) == len(v2):
        sum = 0
        for i in range(len(v1)):
            sum  += v1[i].conjugate()*v2[i]
    else: sum = "Tamaño errado"
    return sum

def vectornormal(v1):
    b = prod_interno(v1, v1)
    b = round(math.sqrt(b.real),2)
    return b

def distancia(v1, v2):
    h = sumavec(v1, inverso(v2))
    dis = vectornormal(h)
    return dis

def sobrevector(k, v1):
    fil_a = len(k)
    col_a = len(k[0])
    fil_v = len(v1)
    if col_a == fil_v:
        vect = []
        for i in range(fil_a):
            sum = 0
            for j in range(col_a):
                sum += k[i][j] * v1[j]
            vect.append(sum)
    else:
        vect = "Verificar entrada"
    return vect

def prod_interno(v1, v2):
    if len(v1) == len(v2):
        sum = 0
        for i in range(len(v1)):
            sum  += v1[i].conjugate()*v2[i]
    else: sum = "Tamaño errado"
    return sum

def vectores_prop(m1):
    m1 = numpy.asarray(m1)
    tam = m1.shape
    fil = tam[0]
    col = tam[1]
    if fil == col:
        val , vecto = numpy.linalg.eig(m1)
        vecto = numpy.transpose(vecto)
        valor = numpy.round(val,2)
        vector = numpy.round(vecto, 2)
        return  "valores: {}. vectores: {}".format(valor, vecto[0])
    else:
        return "Intoduzca una matrz cuadrada"

def unitario(m1):
    if len(m1) == len(m1[0]):
            adjunt = adjunta(m1)
            comp = prod_de_matz(m1, adjunt)
            verifi = True
            for i in range(len(comp)):
                for j in range(len(comp)):
                    if (i == j and comp[i][j] != 1) or (i != j and comp[i][j] != 0):
                        verifi = False
                        break
            if verifi:
                resp = "Es unitaria la matriz"
            else:
                resp = "NO es unitaria la matriz "
    else:
        resp = "Matriz incorrecta de tamaño"
    return resp

def hermitiana(m1):
    if len(m1) == len(m1[0]):
            adjunt = adjunta(m1)
            verifi = True
            for i in range(len(adjunt)):
                for j in range(len(adjunt)):
                    if m1[i][j] != adjunt[i][j]:
                        verifi = False
                        break
            if verifi:
                resp = "Es hermitiana"
            else:
                resp = "NO es hermitiana"
    else:
        resp = "Tamaño de matriz incorrecto"
    return resp

def tensor(m1, m2):
    m = len(m1)
    n = len(m2)
    m_1 = len(m1[0])
    n_1 = len(m2[0])
    fil = m*n
    col = m_1*n_1
    result = [[0 for j in range(col)] for k in range(fil)]
    for j in range(fil):
        for k in range(col):
            result[j][k] = (m1[j // n][k // n_1]) * (m2[j % n][k % n_1])
    return result