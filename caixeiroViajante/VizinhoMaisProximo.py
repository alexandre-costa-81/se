#!/usr/bin/python
# -*- coding: latin-1 -*-

import pcv

# Heurística de contrução do vizinho mais próximo usando o caixeiro viajante
# Autor: Alexandre Gomes da Costa
# Disciplina: Sistemas Evolutivo 2013/2

#print pcv.inicializaMatriz()


def procuraVizinhoProximo(matriz, atual):
	aux = 0
	for i in range(len(matriz[atual])):
		if i == atual:
			i =+ 1
		if aux == 0 and matriz[atual][i] != 0:
			aux =
			


matriz = pcv.inicializaMatriz()



