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
        self.maximo = 2000
        self.lattice_size = 100
        self.initial_density = 0.02
        self.youth_length = 32
        self.mature_length = 32
        self.old_length = 32
        self.dose = 0.4
        self.plague_period = 50

        self.generation = 0

        self.lattice = [
            [0 for y in range(self.lattice_size)]
               for x in range(self.lattice_size)]

        self.lattice_next = [
            [0 for y in range(self.lattice_size)]
               for x in range(self.lattice_size)]

        self.life_time = [
            [0 for y in range(self.lattice_size)]
               for x in range(self.lattice_size)]

        self.youth = [0 for x in range(self.youth_length)]
        self.mature = [0 for x in range(self.mature_length)]
        self.old = [0 for x in range(self.old_length)]

        self.genetic_code = [
            [[youth, mature, old] for y in range(lattice_size)]
            for x in range(lattice_size)]
        
 #   def processo_evolucao(self, iteracao):
        
