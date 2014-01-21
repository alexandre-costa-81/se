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
	l = 2
	m = 2
	n = 2
	L = l+m+n
	#youth = [0 for col in range(l)]
	#maturity = [0 for col in range(m)]
	#old = [0 for col in range(n)]
	alpha = [[[0 for col in range(L)] for row in range(tx)] for col in range(ty)]
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
def geracao(a, aux_cont):
	encontrou = 0
	for j in range(ty):
		for i in range(tx):
			if a[i][j] == 0:
				alpha1, alpha2, encontrou = find_two_mature_neighbors(i, j)
				if encontrou == 2:
					a[i][j] = 1
#					beta1, beta2 = crossover(alpha1,alpha2)

					#alpha[i][j] = beta if random.randint(1,2) == 1 else beta2

					k[i][j] = 1
					#print "a[%d][%d] = %d - TEM: %d VIZINHO(S)" %(i, j, a[i][j], encontrou)
				else:
					print "a[%d][%d] = %d - TEM: %d VIZINHO(S)" %(i, j, a[i][j], encontrou)
			else:
				print "Eveolui celula."

	return a

# --------------------------------------------- #
def find_two_mature_neighbors(i, j):
	alpha1 = []
	alpha2 = []
	numVizinhos = 0

	if a[i][j-1] == 1 and numVizinhos < 2:
		numVizinhos += 1
		if alpha1 == []:
			alpha1 = alpha[i][j-1]
		else:
			alpha2 = alpha[i][j-1]

	if a[i+1][j-1] == 1 and numVizinhos < 2:
		numVizinhos += 1
		if alpha1 == []:
			alpha1 = alpha[i+1][j-1]
		else:
			alpha2 = alpha[i+1][j-1]

	if a[i+1][j] == 1 and numVizinhos < 2:
		numVizinhos += 1
		if alpha1 == []:
			alpha1 = alpha[i+1][j]
		else:
			alpha2 = alpha[i+1][j]

	if a[i+1][j+1] == 1 and numVizinhos < 2:
		numVizinhos += 1
		if alpha1 == []:
			alpha1 = alpha[i+1][j+1]
		else:
			alpha2 = alpha[i+1][j+1]

	if a[i][j+1] == 1 and numVizinhos < 2:
		numVizinhos += 1
		if alpha1 == []:
			alpha1 = alpha[i][j+1]
		else:
			alpha2 = alpha[i][j+1]

	if a[i-1][j+1] == 1 and numVizinhos < 2:
		numVizinhos += 1
		if alpha1 == []:
			alpha1 = alpha[i-1][j+1]
		else:
			alpha2 = alpha[i-1][j+1]

	if a[i-1][j] == 1 and numVizinhos < 2:
		numVizinhos += 1
		if alpha1 == []:
			alpha1 = alpha[i-1][j]
		else:
			alpha2 = alpha[i-1][j]

	if a[i-1][j-1] == 1 and numVizinhos < 2:
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
def p(alpha):
	age = 0
	for col in range(L):
		if col < l:
			if alpha[col] == 1:
				age += 1

		if col >= l and col < l+m:
			if alpha[col] == 1:
				age += 1

		if col >= l+m:
			if alpha[col] == 1:
				age += 1

	return age

# --------------------------------------------- #
def pk():
	return k


def crossover(alpha1, alpha2):
	beta1 = alpha1
	beta2 = alpha2

	m = 3/2

	#beta1 = 

	return beta1, beta2

# --------------------------------------------- #
def monta(a, aux_cont):
	for j in range(ty):
		for i in range(tx):
			if a[i][j] == 0:
				canvas.itemconfig(cell[i][j], fill="black")
			else:
				canvas.itemconfig(cell[i][j], fill="green")

# (Re)define Botões
	global bt1
	global bt2
	bt1 = Button(root, text="PRÓXIMA GERAÇAO", command=lambda: callback(a, aux_cont))
	bt2 = Button(root, text="PLAY", command=lambda: callback_2(a, aux_cont))
	canvas.pack()
	bt1.pack()
	bt2.pack()
	return

#   MAIN   #
if __name__ == "__main__":
	aux_cont = 0
	def_var()

	a[3][3] = 1
	a[4][2] = 1	
	alpha[3][3] = [[1,1],[1,1],[1,1]]
	alpha[4][2] = [[1,0],[0,0],[0,0]]

	print p(alpha[3][3])

	## Variaveis para desenho no ecran
	XY = 10
	root = Tk()
	root.title("Simulador do Ambiênte")

	canvas  = Canvas(root, width=ty*10, height=tx*10, highlightthickness=0, bd=0, bg='black')
	cell = [[0 for row in range(-1,tx+1)] for col in range(-1,ty+1)]

	for j in range(ty):
		for i in range(tx):
			cell[i][j] = canvas.create_oval((i*XY, j*XY, i*XY+XY, j*XY+XY),outline="gray",fill="black")

	monta(a, aux_cont)

	root.mainloop()


