#!/usr/bin/python
# -*- coding: latin-1 -*-
import os, sys

# Módulo para gerar a matriz de contrução do Problema do Caixeiro Viajante
# Autor: Alexandre Gomes da Costa
# Disciplina: Sistemas Evolutivo 2013/2

def inicializaMatriz():
	c1 = [0,2,1,4,9,1]
	c2 = [2,0,5,9,7,2]
	c3 = [1,5,0,3,8,6]
	c4 = [4,9,3,0,2,5]
	c5 = [9,7,8,2,0,2]
	c6 = [1,2,6,5,2,0]

	return [c1,c2,c3,c4,c5,c6]

