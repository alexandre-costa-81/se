#!/usr/bin/python
# -*- coding: latin-1 -*-
import os, sys

# Heurística construtiva do Vizinho Mais Próximo para o problema do Caixeiro Viajante
# Autor: Alexandre Gomes da Costa
# Disciplina: Sistemas Evolutivo 2013/2

## Construindo a matriz
def inicializa():
	## Peso
	c1 = [0,2,1,4,9,1]
	## Valor
	c2 = [2,0,5,9,7,2]
	## Valor
	c3 = [1,5,0,3,8,6]
	## Valor
	c4 = [4,9,3,0,2,5]
	## Valor
	c5 = [9,7,8,2,0,2]
	## Valor
	c6 = [1,2,6,5,2,0]
	## Matriz com o valor das rotas de cada cidade
	matrizCidades = [c1,c2,c3,c4,c5,c6]

	return matrizCidades


print inicializa()


