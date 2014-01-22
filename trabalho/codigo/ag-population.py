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

# GLOBAL



# --------------------------------------------- #
def def_var():
    # DECLARA VARIAVEIS
    ## Variaveis de configuração do automato celular
    global N # Lattice size (N×N)
    global l # tamanho maximo do youth (y)
    global m # tamanho maximo do maturity (m)
    global n # tamanho maximo do old (o)
    global L # tamanho do "Código Genético"
    #global youth
    #global maturity
    #global old
    global alpha # "Código Genético"
    global MAX # maximo de gerações (tempo maximo)
    global a
    global k

    ## Variaveis para desenho no ecran
    global XY # x0, y0, x1, y1
    global root
    global canvas
    global cell
    global tx
    global ty

    # INICIALIZA VARIAVEIS
    ## Variaveis de configuração do automato celular
    tx = 50
    ty = 50
    l = 32
    m = 32
    n = 32
    L = l+m+n
    youth = [0 for col in range(l)]
    maturity = [0 for col in range(m)]
    old = [0 for col in range(n)]
#    alpha = [[[0 for col in range(L)] for row in range(tx)] for col in range(ty)]
    alpha = [[[youth, maturity, old] for row in range(-1,tx+1)] for col in range(-1,ty+1)]
    MAX = 1000
    a = [[0 for row in range(-1,tx+1)] for col in range(-1,ty+1)]
    k = [[0 for row in range(-1,tx+1)] for col in range(-1,ty+1)]

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
    for j in range(ty):
        for i in range(tx):
            if a[i][j] == 0:
                canvas.itemconfig(cell[i][j], fill="white")
            else:
                ageYouth, ageMaturity, ageOld = p(alpha[i][j])
                if k[i][j] <= ageYouth:
                        canvas.itemconfig(cell[i][j], fill="yellow")
                elif k[i][j] > ageYouth and k[i][j] <= (ageYouth + ageMaturity):
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
    for j in range(ty):
        for i in range(tx):
            if a[i][j] == 0:
                alpha1, alpha2, encontrou = find_two_mature_neighbors(i, j)
                if encontrou == 2:
                    a[i][j] = 1
                    beta1, beta2 = crossover(alpha1,alpha2)

                    alpha[i][j] = beta1 if random.randint(1,2) == 1 else beta2
                    #print alpha[i][j]
                    k[i][j] = 1
                    #print "a[%d][%d] = %d - TEM: %d VIZINHO(S)" %(i, j, a[i][j], encontrou)
            else:
                ageYouth, ageMaturity, ageOld = p(alpha[i][j])
                age = ageYouth + ageMaturity + ageOld
                if pk(alpha[i][j],k[i][j]) == age:
                #if k[i][j] > p(alpha[i][j]):
                #if k[i][j] > age:
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

    ageYouth, ageMaturity, ageOld = p(alpha[i][j-1])
    if a[i][j-1] == 1 and numVizinhos < 2 and k[i][j-1] > ageYouth and k[i][j-1] <= (ageYouth + ageMaturity):
        numVizinhos += 1
        if alpha1 == []:
            alpha1 = alpha[i][j-1]
        else:
            alpha2 = alpha[i][j-1]

    ageYouth, ageMaturity, ageOld = p(alpha[i+1][j-1])
    if a[i+1][j-1] == 1 and numVizinhos < 2 and k[i+1][j-1] > ageYouth and k[i+1][j-1] <= (ageYouth + ageMaturity):
        numVizinhos += 1
        if alpha1 == []:
            alpha1 = alpha[i+1][j-1]
        else:
            alpha2 = alpha[i+1][j-1]


    ageYouth, ageMaturity, ageOld = p(alpha[i+1][j])
    if a[i+1][j] == 1 and numVizinhos < 2 and k[i+1][j] > ageYouth and k[i+1][j] <= (ageYouth + ageMaturity):
        numVizinhos += 1
        if alpha1 == []:
            alpha1 = alpha[i+1][j]
        else:
            alpha2 = alpha[i+1][j]

    ageYouth, ageMaturity, ageOld = p(alpha[i+1][j+1])
    if a[i+1][j+1] == 1 and numVizinhos < 2 and k[i+1][j+1] > ageYouth and k[i+1][j+1] <= (ageYouth + ageMaturity):
        numVizinhos += 1
        if alpha1 == []:
            alpha1 = alpha[i+1][j+1]
        else:
            alpha2 = alpha[i+1][j+1]

    ageYouth, ageMaturity, ageOld = p(alpha[i][j+1])
    if a[i][j+1] == 1 and numVizinhos < 2 and k[i][j+1] > ageYouth and k[i][j+1] <= (ageYouth + ageMaturity):
        numVizinhos += 1
        if alpha1 == []:
            alpha1 = alpha[i][j+1]
        else:
            alpha2 = alpha[i][j+1]

    ageYouth, ageMaturity, ageOld = p(alpha[i-1][j+1])
    if a[i-1][j+1] == 1 and numVizinhos < 2 and k[i-1][j+1] > ageYouth and k[i-1][j+1] <= (ageYouth + ageMaturity):
        numVizinhos += 1
        if alpha1 == []:
            alpha1 = alpha[i-1][j+1]
        else:   
            alpha2 = alpha[i-1][j+1]


    ageYouth, ageMaturity, ageOld = p(alpha[i-1][j])
    if a[i-1][j] == 1 and numVizinhos < 2 and k[i-1][j] > ageYouth and k[i-1][j] <= (ageYouth + ageMaturity):
        numVizinhos += 1
        if alpha1 == []:
            alpha1 = alpha[i-1][j]
        else:
            alpha2 = alpha[i-1][j]


    ageYouth, ageMaturity, ageOld = p(alpha[i-1][j-1])
    if a[i-1][j-1] == 1 and numVizinhos < 2 and k[i-1][j-1] > ageYouth and k[i-1][j-1] <= (ageYouth + ageMaturity):
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
    maturity1 = 0
    old1 = 0

    for x1 in range(3):
        if x1 == 0:
            for y1 in range(l):
                if _alpha[x1][y1] == 1:
                    youth1 += 1
        if x1 == 1:
            for y1 in range(m):
                if _alpha[x1][y1] == 1:
                    maturity1 += 1
        if x1 == 2:
            for y1 in range(n):
                if _alpha[x1][y1] == 1:
                    old1 += 1

    age = youth1, maturity1, old1
            
#    for col in range(L):
#        if alpha[col] == 1:
#            age += 1

    return age

# --------------------------------------------- #
def pk(alpha, k):

    ageYouth, ageMaturity, ageOld = p(alpha)

    if (ageYouth + ageMaturity + ageOld) >= k:
        return k
    else:
        return (ageYouth + ageMaturity + ageOld)


def crossover(alpha1, alpha2):
    beta1 = alpha1
    beta2 = alpha2

    for tripla in range(3):
        if tripla == 0:
            medio = l/2
        elif tripla == 1:
            medio = m/2
        elif tripla == 2:
            medio = n/2

        beta1[tripla] = alpha1[tripla][:medio] + alpha2[tripla][medio:]
        beta2[tripla] = alpha2[tripla][:medio] + alpha1[tripla][medio:]
        

#    medio = L/2

#    beta1 = alpha1[:medio] + alpha2[medio:]
#    beta2 = alpha2[:medio] + alpha1[medio:]

    return beta1, beta2


# --------------------------------------------- #
def gera_populacao(p0):
    for x in range(int(tx*ty*p0)):
        i1 = random.randint(0,tx-1)
        j1 = random.randint(0,ty-1)
        
        a[i1][j1] = 1
        k[i1][j1] = 1

        print i1, j1
        
#        for y in range(L):
#            alpha[i1][j1][y] = random.randint(0,1)
        for tripla in range(3):
            if tripla == 0:
                for y1 in range(l):
                    y2 = 1 if random.random() > 0.5 else 0
                    alpha[i1][j1][tripla][y1] = y2
            if tripla == 1:
                for m1 in range(m):
                    m2 = 1 if random.random() > 0.5 else 0
                    alpha[i1][j1][tripla][m1] = m2
            if tripla == 2:
                for o1 in range(n):
                    o2 = 1 if random.random() > 0.5 else 0
                    alpha[i1][j1][tripla][o1] = o2
        
        
    return 



#   MAIN   #
if __name__ == "__main__":
    aux_cont = 0
    def_var()
    p0 = 0.02

    #print alpha[0][0]
    #print a[0][0]
    gera_populacao(p0)


    #print p(alpha[0][0])
    print alpha[0][0]
    print alpha[10][5]
    #print a[0][0]
#    a[3][3] = 1
#    a[4][2] = 1 
#    alpha[3][3] = [1,1,1,0,0,0]
#    alpha[4][2] = [0,0,0,1,1,1]
#    k[3][3] = 1
#    k[4][2] = 1

    ## Variaveis para desenho no ecran
    XY = 10
    root = Tk()
    root.title("Simulador do Ambiênte")

    canvas  = Canvas(root, width=ty*10, height=tx*10, highlightthickness=0, bd=0, bg='white')
    cell = [[0 for row in range(-1,tx+1)] for col in range(-1,ty+1)]

    for j in range(ty):
        for i in range(tx):
            cell[i][j] = canvas.create_oval((i*XY, j*XY, i*XY+XY, j*XY+XY),outline="gray",fill="white")

    monta(a, aux_cont)

    root.mainloop()


