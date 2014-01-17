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


## Variaveis de configuração do automato celular
N = 50 # Lattice size (N×N)
l = 2 # tamanho maximo do youth (y)
m = 2 # tamanho maximo do maturity (m)
n = 2 # tamanho maximo do old (o)
L = l+m+n # tamanho do "Código Genético"
y = [0 for col in range(l)] # 
m = [0 for col in range(m)]
o = [0 for col in range(n)]
alpha = [[[y, m, o] for j in range(N)] for i in range(N)] # "Código Genético"
MAX = 1000 # maximo de gerações (tempo maximo)
a = [[0 for j in range(N)] for i in range(N)] 

k = [[0 for j in range(N)] for i in range(N)]

## Variaveis para desenho no ecran
XY = 10 # x0, y0, x1, y1
cell = [[0 for j in range(N)] for i in range(N)]



# FUNCTIONS
## Funções para desenho no ecran
def carrega():
	for i in range(N):
		for j in range(N):
			cell[i][j] = canvas.create_oval((i*XY, j*XY, i*XY+XY, j*XY+XY),outline="gray",fill="black")

def frame():
#	processa()
	desenha()
	root.after(100, frame)

def desenha():
	for i in range(N):
		for j in range(N):
			if a[i][j]==0:
				canvas.itemconfig(cell[i][j], fill="black")
			if a[i][j]==1:
				canvas.itemconfig(cell[i][j], fill="green")

## Funções do automato celular
def evolucao():
	for t in range(MAX):
		for i in range(N):
			for i in range(N):
				if a[i][j] == 0:
					vizinho1, vizinho2, encontrou = encontraDoisVizinhosMaduros(i, j)

					if encontrou = 1:
						a[i][j] = 1

						alpha[i][j] = vizinho1

						k[i][j] = 1
					else:
						if p(alpha[i][j]) == L:
							a[i][j] = 0
							k[i][j] = 0
						else
							a[i][j] = 1
				else:
					k = 1

def encontraDoisVizinhosMaduros(i, j):
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



# MAIN
root = Tk()
root.title("Simulador do Ambiênte")
canvas = Canvas(root, width=500, height=500, highlightthickness=0, bd=0, bg='black')
canvas.pack()
carrega()
frame()
root.mainloop()

