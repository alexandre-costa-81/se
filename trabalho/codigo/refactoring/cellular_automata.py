# -*- coding: utf-8 -*-

"""
Created: 15/01/2014
@autor: Alexandre Costa
@disciplina: Sistemas Evolutivos
@professor: Marilton Aguiar
@descrição: trabalho final da @disciplina, onde foi desenvolvido um Algoritmo de
 Busca Tabu que simula o ataque de pragas periódicas a um conjunto de colonias.
"""

import random
from copy import copy, deepcopy

class CellularAutomata:
    maximo = None
    lattice_size = None
    initial_density = None
    youth_length = None
    mature_length = None
    old_length = None
    dose = None
    plague_period = None

    population = None
    population_youth = None
    population_mature = None
    population_old = None

    generation = None
    
    lattice = []
    life_time = []
       
    youth = []
    mature = []
    old = []
    
    genetic_code = []

    def __init__(self, 
            maximo=2000, 
            lattice_size=10, 
            initial_density=0.02, 
            youth_length=2,
            mature_length=2,
            old_length=2,
            dose=0.4,
            plague_period=50
    ):
        self.maximo = maximo
        self.lattice_size = lattice_size
        self.initial_density = initial_density
        self.youth_length = youth_length
        self.mature_length = mature_length
        self.old_length = old_length
        self.dose = dose
        self.plague_period = plague_period
        
        self.population = 0
        self.population_youth = 0
        self.population_mature = 0
        self.population_old = 0

        self.generation = 0

        self.lattice = [
            [0 for y in range(self.lattice_size)]
               for x in range(self.lattice_size)]

        self.life_time = [
            [0 for y in range(self.lattice_size)]
               for x in range(self.lattice_size)]

        self.youth = [0 for x in range(self.youth_length)]
        self.mature = [0 for x in range(self.mature_length)]
        self.old = [0 for x in range(self.old_length)]

        self.genetic_code = [
            [[self.youth, self.mature, self.old]
            for y in range(self.lattice_size)]
            for x in range(self.lattice_size)]
        
    def generate_population(self, initial_density):
        lattice_next = deepcopy(self.lattice)
        life_time_next = deepcopy(self.life_time)
        genetic_code_next = deepcopy(self.genetic_code)
        
        if initial_density != 0:
            self.initial_density = initial_density 
        
        x = 0
        print self.initial_density
        while x < int(self.lattice_size*self.lattice_size*self.initial_density):
            i1 = random.randint(0,self.lattice_size-1)
            j1 = random.randint(0,self.lattice_size-1)

            randBinList = lambda n: [random.randint(0,1) for b in range(1,n+1)]
        
            if lattice_next[i1][j1] == 1:
                x -= 1
            else:
                lattice_next[i1][j1] = 1
                life_time_next[i1][j1] = 1

                genetic_code_next[i1][j1][0] = randBinList(self.youth_length)
                genetic_code_next[i1][j1][1] = randBinList(self.mature_length)
                genetic_code_next[i1][j1][2] = randBinList(self.old_length)
        
            x += 1

        return x, lattice_next, life_time_next, genetic_code_next

    def number_ones_genetic_code(self, alpha):
        age = 0
        youth = 0
        mature = 0
        old = 0

        for x in range(3):
            if x == 0:
                for y in range(self.youth_length):
                    if alpha[x][y] == 1:
                        youth += 1
            if x == 1:
                for y in range(self.mature_length):
                    if alpha[x][y] == 1:
                        mature += 1
            if x == 2:
                for y in range(self.old_length):
                    if alpha[x][y] == 1:
                        old += 1


        age = youth, mature, old
        
        return age

    def move_individuals(self):
        deepcopy1d2d = lambda lVals: [x if not isinstance(x, list) else x[:] for x in lVals]
        self.lattice_next = map(list, self.lattice)
        cpy = deepcopy(self.lattice)
        print(id(cpy), id(self.lattice))
        #self.life_time_next = self.life_time[:]
        #self.genetic_code_next = self.genetic_code[:]
        #print(self.lattice_next is self.lattice)
#        selecionado = random.randint(0,7)

#        if selecionado == 0 and j > 0:
#            if self.lattice[i][j-1] == 0 and self.lattice_next[i][j-1] == 0:
        for i in range(self.lattice_size):
            for j in range(self.lattice_size):
                if self.lattice[i][j] == 1 and j < (self.lattice_size-1):# and self.lattice[i][j+1] == 0 and self.lattice_next[i][j+1] != 1:
                    cpy[i][j+1] = int(1)
                    print(id(cpy[i][j+1]), id(self.lattice[i][j+1]))
                    print(id(cpy[i][j]), id(self.lattice[i][j]))
                    #self.lattice_next[i][j+1] = self.life_time[i][j]
                    #self.genetic_code_next[i][j+1] = self.genetic_code[i][j]
                    cpy[i][j] = 0
                    #self.life_time_next[i][j] = 0
                    #self.genetic_code_next[i][j] = [self.youth, self.mature, self.old]
                    #print(self.lattice_next is self.lattice)
                    #print ("Lattice", self.lattice[i][j])
                    #print ("Lattice Next", self.lattice_next[i][j])
                    raw_input()
                    
        self.lattice = deepcopy(cpy)
        #self.life_time = self.life_time_next
        #self.genetic_code = self.genetic_code_next
        
    def printMatrix(self, testMatrix):
        print ' ',
        for i in range(len(testMatrix[1])):  # Make it work with non square matrices.
            print i,
        print
        for i, element in enumerate(testMatrix):
            print i, ' '.join(str(element))

def main():
    
    ca = CellularAutomata()
    
    ca.population, ca.lattice, ca.life_time, ca.genetic_code = ca.generate_population(0)
    
    #print ("Population",ca.population)
    #print ("Lattice", ca.lattice)
    #print ("Life_Time", ca.life_time)
    #print ("genetic_code", ca.genetic_code)
    
    ca.printMatrix(ca.lattice)
    
    ca.move_individuals()
    
    ca.printMatrix(ca.lattice)
    

if __name__ == "__main__":
    main()

        
