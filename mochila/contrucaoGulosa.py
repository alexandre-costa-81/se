#!/usr/bin/python
# -*- coding: latin-1 -*-
import os, sys

# Contrução Gulosa do Problema da Mochila
# Autor: Alexandre Gomes da Costa
# Disciplina: Sistemas Evolutivo 2013/2


## Inicializa a matriz
def inicializaC():
	## Peso
	w = [4,5,7,9,6]
	## Valor
	p = [2,2,3,4,4]
	## Objetos
	j = [w,p]

	return j

## Retira o melhor elemento
def melhor(lista):
	aux = 0
	for i in range(len(lista[0])):
		if lista[1][i] > lista[1][aux]:
			aux = i
		elif lista[1][i] == lista[1][aux]:
			if lista[0][i] < lista[0][aux]:
				aux = i
	return aux



## function ConstrucaoGulosa
def construcaoGulosa():
	s = [[],[]]
	c = inicializaC()
	print c
	for i in range(len(c[0])):
		m = melhor(c)
		s[0].insert(len(s[0]),c[0].pop(m))
		s[1].insert(len(s[1]),c[1].pop(m))
	return s


## main
print construcaoGulosa()
