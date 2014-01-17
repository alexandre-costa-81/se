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
	global y
	global m
	global o
	global alpha # "Código Genético"
	global MAX # maximo de gerações (tempo maximo)
	global a
	global k

	## Variaveis para desenho no ecran
	global XY # x0, y0, x1, y1
	global root
	global canvas
	global cell

	# INICIALIZA VARIAVEIS
	## Variaveis de configuração do automato celular
	N = 51
	l = 2
	m = 2
	n = 2
	L = l+m+n
	y = [0 for col in range(l)]
	m = [0 for col in range(m)]
	o = [0 for col in range(n)]
	alpha = [[[y, m, o] for j in range(N)] for i in range(N)]
	MAX = 1000
	a = [[0 for j in range(-1, N)] for i in range(-1, N)] 
	k = [[0 for j in range(-1, N)] for i in range(-1, N)] 

	## Variaveis para desenho no ecran
	XY = 10
	root = Tk()
	root.title("Simulador do Ambiênte")
	canvas = Canvas(root, width=500, height=500, highlightthickness=0, bd=0, bg='black')
	cell = [[0 for j in range(-1, N)] for i in range(-1, N)]
	for i in range(N):
		for j in range(N):
			cell[i][j] = canvas.create_oval((i*XY, j*XY, i*XY+XY, j*XY+XY),outline="gray",fill="black")

# --------------------------------------------- #
def callback(a, aux_cont):
    aux_cont = aux_cont + 1
    print "t = %d" %(aux_cont+1)
    destroy_bt()
    a = geracao(a, aux_cont)
    monta(a, aux_cont)

# --------------------------------------------- #
def callback_2(a, aux_cont):
    aux_cont = aux_cont + 1
    print "t = %d" %(aux_cont+1)
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
	for i in range(N):
		for j in range(N):
			if a[i][j] == 0:
				canvas.itemconfig(cell[i][j], fill="black")
			else:
				canvas.itemconfig(cell[i][j], fill="green")
	canvas.pack()

	for i in range(N):
		for j in range(N):
			if a[i][j] == 0:
				vizinho1, vizinho2, encontrou = retornaVizinhaca(i, j)
				print i, j
				if encontrou == 1:
					a[i][j] = 1
					alpha[i][j] = vizinho1
					
					#k[i][j] = 1
				else:
					#if p(alpha[i][j]) == L:
					a[i][j] = 0
					k[i][j] = 0
					#else:
					#	a[i][j] = 1
			else:
				a[i][j] = 1
#				k = 1

	return a

# --------------------------------------------- #
def retornaVizinhaca(i, j):
	vizinho1 = []
	vizinho2 = []
	if a[i][j-1] == 1:
		vizinho1 = alpha[i][j-1]
	elif a[i+1][j-1] == 1:
		if vizinho1 == []:
			vizinho1 = alpha[i+1][j-1]
		else:
			vizinho2 = alpha[i+1][j-1]
	elif a[i+1][j] == 1:
		if vizinho1 == []:
			vizinho1 = alpha[i+1][j]
		else:
			vizinho2 = alpha[i+1][j]
	elif a[i+1][j+1] == 1:
		if vizinho1 == []:
			vizinho1 = alpha[i+1][j+1]
		else:
			vizinho2 = alpha[i+1][j+1]
	elif a[i][j+1] == 1:
		if vizinho1 == []:
			vizinho1 = alpha[i][j+1]
		else:
			vizinho2 = alpha[i][j+1]
	elif a[i-1][j+1] == 1:
		if vizinho1 == []:
			vizinho1 = alpha[i-1][j+1]
		else:
			vizinho2 = alpha[i-1][j+1]
	elif a[i-1][j] == 1:
		if vizinho1 == []:
			vizinho1 = alpha[i-1][j]
		else:
			vizinho2 = alpha[i-1][j]
	elif a[i-1][j-1] == 1:
		if vizinho1 == []:
			vizinho1 = alpha[i-1][j-1]
		else:
			vizinho2 = alpha[i-1][j-1]

	if vizinho1 == [] or vizinho1 == []:
		return vizinho1, vizinho2, 0
	else:
		return vizinho1, vizinho2, 1


# --------------------------------------------- #
def monta(a, aux_cont):
	for i in range(N):
		for j in range(N):
			if a[i][j] == 0:
				canvas.itemconfig(cell[i][j], fill="black")
			else:
				canvas.itemconfig(cell[i][j], fill="green")

    # (Re)define Botões
	global bt1
	global bt2
	bt1 = Button(root, text="PRÓXIMA GERAÇAO", command=lambda: callback(m, n, aux_cont))
	bt2 = Button(root, text="PLAY", command=lambda: callback_2(m, n, aux_cont))
	bt1.pack()
	bt2.pack()
	canvas.pack()
    #

	if aux_cont == 0:
		print 'nnn1'
		root.mainloop()
		def_var()

	return

#   MAIN   #
if __name__ == "__main__":
	aux_cont = 0
	def_var()

	a = [[0 for j in range(-1, N)] for i in range(-1, N)] 
	a[3][3] = 1
	a[4][2] = 1	
	alpha[3][3] = [[0,1],[0,0],[0,0]]
	alpha[4][2] = [[0,1],[0,0],[0,0]]

	a = geracao(a, aux_cont)
	monta(a, aux_cont)

"""

def frame():
#	processa()
	geracao()
	desenha()
	root.after(100, frame)

def desenha():
	for i in range(N):
		for j in range(N):
			if a[i][j]==0:
				canvas.itemconfig(cell[i][j], fill="black")
			else:
				canvas.itemconfig(cell[i][j], fill="green")

## Funções do automato celular
def geracao():
	for i in range(N):
		for j in range(N):
			if a[i][j] == 0:
				vizinho1, vizinho2, encontrou = retornaVizinhaca(i, j)
				print i, j
				if encontrou == 1:
					a[i][j] = 1
					alpha[i][j] = vizinho1
					
					#k[i][j] = 1
				else:
					if p(alpha[i][j]) == L:
						a[i][j] = 0
						k[i][j] = 0
					else:
						a[i][j] = 1
			else:
				k = 1

	for i in range(N):
		for j in range(N):
			if a[i][j] == 0:
				canvas.itemconfig(cell[i][j], fill="black")
			else:
				canvas.itemconfig(cell[i][j], fill="green")
    #canvas.pack()
	return

def retornaVizinhaca(i, j):
	vizinho1 = []
	vizinho2 = []
	if a[i][j-1] == 1:
		vizinho1 = alpha[i][j-1]
	elif a[i+1][j-1] == 1:
		if vizinho1 == []:
			vizinho1 = alpha[i+1][j-1]
		else:
			vizinho2 = alpha[i+1][j-1]
	elif a[i+1][j] == 1:
		if vizinho1 == []:
			vizinho1 = alpha[i+1][j]
		else:
			vizinho2 = alpha[i+1][j]
	elif a[i+1][j+1] == 1:
		if vizinho1 == []:
			vizinho1 = alpha[i+1][j+1]
		else:
			vizinho2 = alpha[i+1][j+1]
	elif a[i][j+1] == 1:
		if vizinho1 == []:
			vizinho1 = alpha[i][j+1]
		else:
			vizinho2 = alpha[i][j+1]
	elif a[i-1][j+1] == 1:
		if vizinho1 == []:
			vizinho1 = alpha[i-1][j+1]
		else:
			vizinho2 = alpha[i-1][j+1]
	elif a[i-1][j] == 1:
		if vizinho1 == []:
			vizinho1 = alpha[i-1][j]
		else:
			vizinho2 = alpha[i-1][j]
	elif a[i-1][j-1] == 1:
		if vizinho1 == []:
			vizinho1 = alpha[i-1][j-1]
		else:
			vizinho2 = alpha[i-1][j-1]

	if vizinho1 == [] or vizinho1 == []:
		return vizinho1, vizinho2, 0
	else:
		return vizinho1, vizinho2, 1

def cruzamentoGenetico():
	return 0

def p(alphaij):
	return 0

def pk(alphaij):
	return 0

def geraPopulacao():
	a[3][3] = 1
	a[4][2] = 1	
	alpha[3][3] = [[0,1],[0,0],[0,0]]
	alpha[4][2] = [[0,1],[0,0],[0,0]]


# MAIN

canvas.pack()
geraPopulacao()
carrega()
frame()
root.mainloop()
"""


