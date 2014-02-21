# -*- coding: utf-8 -*-

"""
Created: 15/01/2014
@autor: Alexandre Costa
@disciplina: Sistemas Evolutivos
@professor: Marilton Aguiar
@descrição: trabalho final da @disciplina, onde foi desenvolvido um Algoritmo de
 Busca Tabu que simula o ataque de pragas periódicas a um conjunto de colonias.
"""

class AutomatoCelular:
    def __init__(self):
        self.maximo=2000
        self.malha_tamanho=100
        self.densidade_inicial=0.02
        self.cromossomo_jovem=32
        self.cromossomo_maduro=32
        self.cromossomo_velho=32
        self.quantidade_praga=0.4
        self.praga_periodo=50

        self.geracao=0
        self.malha=[[0 for y in range(self.malha_tamanho)] 
                       for x in range(self.malha_tamanho)]
        self.cromossomo_idade=[[0 for y in range(self.malha_tamanho)] 
                                  for x in range(self.malha_tamanho)]

 #   def processo_evolucao(self, iteracao):
        
