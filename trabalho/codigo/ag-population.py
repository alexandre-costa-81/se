# -*- coding: utf-8 -*-
"""
Created: 15/01/2014
@autor: Alexandre Costa
@disciplina: Sistemas Evolutivos
@professor: Marilton Aguiar
@descrição: trabalho final da @disciplina, onde foi desenvolvido um Algoritmo Genético que simula o ataque de pragas periódicas a um conjunto de colonias.
"""

# Packages
from Tkinter import *
import random
import time
from datetime import datetime

# GLOBAL



# --------------------------------------------- #
def def_var():
    # DECLARA VARIAVEIS
    ## Variaveis de configuração do automato celular
    global N # Lattice size (N×N)
    global l # tamanho maximo do youth (y)
    global m # tamanho maximo do maturiN (m)
    global n # tamanho maximo do old (o)
    global L # tamanho do "Código Genético"
    global alpha # "Código Genético"
    global MAX # maximo de gerações (tempo maximo)
    global a
    global k

    ## Variaveis para desenho no ecran
    global XY # x0, y0, x1, y1
    global root
    global canvas
    global cell
    global N
    global N

# --------------------------------------------- #
def callback(a, aux_cont):
        aux_cont = aux_cont + 1
        print "Tempo = %d" %(aux_cont)
        destroy_bt()
        a = geracao(a, aux_cont)
        monta(a, aux_cont)

# --------------------------------------------- #
def callback_2(a, aux_cont):
        aux_cont = aux_cont + 1
        print "Tempo = %d" %(aux_cont)
        destroy_bt()
        a = geracao(a, aux_cont)
        monta(a, aux_cont)
        root.after(100,lambda: callback_2(a, aux_cont))

# --------------------------------------------- #
def destroy_bt():
        bt1.destroy()
        bt2.destroy()


# --------------------------------------------- #
def monta(a, aux_cont):
    for j in range(N):
        for i in range(N):
            if a[i][j] == 0:
                canvas.itemconfig(cell[i][j], fill="white")
            else:
                ageYouth, ageMaturiN, ageOld = p(alpha[i][j])
                if k[i][j] <= ageYouth:
                        canvas.itemconfig(cell[i][j], fill="yellow")
                elif k[i][j] > ageYouth and k[i][j] <= (ageYouth + ageMaturiN):
                        canvas.itemconfig(cell[i][j], fill="red")
                else:
                        canvas.itemconfig(cell[i][j], fill="blue")

# (Re)define Botões
    global bt1
    global bt2
    bt1 = Button(root, text="PRÓXIMA GERAÇAO", command=lambda: callback(a, aux_cont))
    bt2 = Button(root, text="PLAY", command=lambda: callback_2(a, aux_cont))
    canvas.pack()
    bt1.pack()
    bt2.pack()
    return


# --------------------------------------------- #
def geracao(a, aux_cont):
    encontrou = 0
    for j in range(N):
        for i in range(N):
            if a[i][j] == 0:
                alpha1, alpha2, encontrou = find_two_mature_neighbors(i, j)
                if encontrou == 2:
                    a[i][j] = 1
                    beta1, beta2 = crossover(alpha1,alpha2)

                    alpha[i][j] = beta1 if random.random() > 0.5 else beta2

                    k[i][j] = 1
            else:
                ageYouth, ageMaturiN, ageOld = p(alpha[i][j])
                age = ageYouth + ageMaturiN + ageOld
                if pk(alpha[i][j],k[i][j]) == age:
                    k[i][j] = 0
                    a[i][j] = 0
                else:
                    k[i][j] = pk(alpha[i][j],k[i][j])
                    k[i][j] += 1

    return a

# --------------------------------------------- #
def find_two_mature_neighbors(i, j):
    alpha1 = []
    alpha2 = []
    numVizinhos = 0

    ageYouth, ageMaturiN, ageOld = p(alpha[i][j-1])
    if a[i][j-1] == 1 and numVizinhos < 2 and k[i][j-1] > ageYouth and k[i][j-1] <= (ageYouth + ageMaturiN):
        numVizinhos += 1
        if alpha1 == []:
            alpha1 = alpha[i][j-1]
        else:
            alpha2 = alpha[i][j-1]

    ageYouth, ageMaturiN, ageOld = p(alpha[i+1][j-1])
    if a[i+1][j-1] == 1 and numVizinhos < 2 and k[i+1][j-1] > ageYouth and k[i+1][j-1] <= (ageYouth + ageMaturiN):
        numVizinhos += 1
        if alpha1 == []:
            alpha1 = alpha[i+1][j-1]
        else:
            alpha2 = alpha[i+1][j-1]


    ageYouth, ageMaturiN, ageOld = p(alpha[i+1][j])
    if a[i+1][j] == 1 and numVizinhos < 2 and k[i+1][j] > ageYouth and k[i+1][j] <= (ageYouth + ageMaturiN):
        numVizinhos += 1
        if alpha1 == []:
            alpha1 = alpha[i+1][j]
        else:
            alpha2 = alpha[i+1][j]

    ageYouth, ageMaturiN, ageOld = p(alpha[i+1][j+1])
    if a[i+1][j+1] == 1 and numVizinhos < 2 and k[i+1][j+1] > ageYouth and k[i+1][j+1] <= (ageYouth + ageMaturiN):
        numVizinhos += 1
        if alpha1 == []:
            alpha1 = alpha[i+1][j+1]
        else:
            alpha2 = alpha[i+1][j+1]

    ageYouth, ageMaturiN, ageOld = p(alpha[i][j+1])
    if a[i][j+1] == 1 and numVizinhos < 2 and k[i][j+1] > ageYouth and k[i][j+1] <= (ageYouth + ageMaturiN):
        numVizinhos += 1
        if alpha1 == []:
            alpha1 = alpha[i][j+1]
        else:
            alpha2 = alpha[i][j+1]

    ageYouth, ageMaturiN, ageOld = p(alpha[i-1][j+1])
    if a[i-1][j+1] == 1 and numVizinhos < 2 and k[i-1][j+1] > ageYouth and k[i-1][j+1] <= (ageYouth + ageMaturiN):
        numVizinhos += 1
        if alpha1 == []:
            alpha1 = alpha[i-1][j+1]
        else:   
            alpha2 = alpha[i-1][j+1]


    ageYouth, ageMaturiN, ageOld = p(alpha[i-1][j])
    if a[i-1][j] == 1 and numVizinhos < 2 and k[i-1][j] > ageYouth and k[i-1][j] <= (ageYouth + ageMaturiN):
        numVizinhos += 1
        if alpha1 == []:
            alpha1 = alpha[i-1][j]
        else:
            alpha2 = alpha[i-1][j]


    ageYouth, ageMaturiN, ageOld = p(alpha[i-1][j-1])
    if a[i-1][j-1] == 1 and numVizinhos < 2 and k[i-1][j-1] > ageYouth and k[i-1][j-1] <= (ageYouth + ageMaturiN):
        numVizinhos += 1
        if alpha1 == []:
            alpha1 = alpha[i-1][j-1]
        else:
            alpha2 = alpha[i-1][j-1]

    if numVizinhos == 2:
        return alpha1, alpha2, numVizinhos
    else:
        return alpha1, alpha2, numVizinhos

# --------------------------------------------- #
def p(_alpha):
    age = 0
    youth1 = 0
    maturiN1 = 0
    old1 = 0

    for x1 in range(3):
        if x1 == 0:
            for y1 in range(l):
                if _alpha[x1][y1] == 1:
                    youth1 += 1
        if x1 == 1:
            for y1 in range(m):
                if _alpha[x1][y1] == 1:
                    maturiN1 += 1
        if x1 == 2:
            for y1 in range(n):
                if _alpha[x1][y1] == 1:
                    old1 += 1

    age = youth1, maturiN1, old1
            
#    for col in range(L):
#        if alpha[col] == 1:
#            age += 1

    return age

# --------------------------------------------- #
def pk(alpha, k):

    ageYouth, ageMaturiN, ageOld = p(alpha)

    if (ageYouth + ageMaturiN + ageOld) >= k:
        return k
    else:
        return (ageYouth + ageMaturiN + ageOld)


def crossover(alpha1, alpha2):
    beta1 = alpha1
    beta2 = alpha2

    beta1[0] = alpha1[0][:(l/2)] + alpha2[0][(l/2):]
    beta2[0] = alpha2[0][:(l/2)] + alpha1[0][(l/2):]
    beta1[1] = alpha1[1][:(m/2)] + alpha2[1][(m/2):]
    beta2[1] = alpha2[1][:(m/2)] + alpha1[1][(m/2):]
    beta1[2] = alpha1[2][:(n/2)] + alpha2[2][(n/2):]
    beta2[2] = alpha2[2][:(n/2)] + alpha1[2][(n/2):]

    return beta1, beta2


# --------------------------------------------- #
def gera_populacao(p0):
    for x in range(int(N*N*p0)):
        i1 = random.randint(0,N-1)
        j1 = random.randint(0,N-1)

        randBinList = lambda n: [random.randint(0,1) for b in range(1,n+1)]

        a[i1][j1] = 1
        k[i1][j1] = 1

        alpha[i1][j1][0] = randBinList(l)

        alpha[i1][j1][1] = randBinList(m)

        alpha[i1][j1][2] = randBinList(n)

    return



#   MAIN   #
if __name__ == "__main__":
    aux_cont = 0
    def_var()


### CONFIGURAÇÃO DO SISTEMA ###
    p0 = 0.90   # Initial densiN (P0)
    N = 50      # Lattice size (N×N)
    l = 32      # Youth   - length
    m = 32      # Mature  - length
    n = 32      # Old age - length
### ----------------------- ###

    # INICIALIZA VARIAVEIS
    ## Variaveis de configuração do automato celular
    L = l+m+n
    youth = [0 for col in range(l)]
    maturiN = [0 for col in range(m)]
    old = [0 for col in range(n)]
    alpha = [[[youth, maturiN, old] for row in range(-1,N+1)] for col in range(-1,N+1)]
    a = [[0 for row in range(-1,N+1)] for col in range(-1,N+1)]
    k = [[0 for row in range(-1,N+1)] for col in range(-1,N+1)]

    gera_populacao(p0)

    ## Variaveis para desenho no ecran
    XY = 10
    root = Tk()
    root.title("Simulador do Ambiênte")

    canvas  = Canvas(root, width=N*10, height=N*10, highlightthickness=0, bd=0, bg='white')
    cell = [[0 for row in range(-1,N+1)] for col in range(-1,N+1)]

    for j in range(N):
        for i in range(N):
            cell[i][j] = canvas.create_oval((i*XY, j*XY, i*XY+XY, j*XY+XY),outline="gray",fill="white")

    monta(a, aux_cont)

    root.mainloop()


