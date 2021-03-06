#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import random
import string
import crypt
import os


class Individual:

    def __init__(self, size, cipher, genome=[], mutation_rate=0.1):
        self._size = size
        self._cipher = cipher
        self._mutation_rate = mutation_rate
        self._fitness = 0
        if genome == []:
            self._genome = [random.choice(string.ascii_lowercase) for _ in range(size)]
        else:
            self._genome = genome
            self.mutation()
        self.compute_fitness()

    def __str__(self):
        return '%s [size = %d, fitness = %d]' % (''.join(self._genome), self._size, self._fitness)

    @property
    def genome(self):
        return self._genome

    @property
    def fitness(self):
        return self._fitness

    @property
    def size(self):
        return self._size

    def crossover(self, other):
        point = random.randint(0, min(self._size, other.size) - 1)
        child1_genome = self._genome[:point] + other.genome[point:]
        child2_genome = other.genome[:point] + self._genome[point:]
        child1 = Individual(len(child1_genome), self._cipher, child1_genome, self._mutation_rate)
        child2 = Individual(len(child2_genome), self._cipher, child2_genome, self._mutation_rate)
        return child1, child2

    def mutation(self):
        if random.random() < self._mutation_rate:
            point = random.randint(0, self._size - 1)
            self._genome[point] = chr((ord(self._genome[point]) - ord('a') + random.randint(0, 26)) % 26 + ord('a'))

    def compute_fitness(self):
        plain = crypt.decrypt(''.join(self._genome), self._cipher)
        self._fitness = plain.count('e') + plain.count('s')
        return self._fitness


def next(pop):
    pos = int(len(pop) / 2)
    pop = sorted(pop, key=lambda x: x.fitness)[pos:]
    best = pop[-1]
    i = 0
    while i + 1 < pos:
        pop.extend(pop[i].crossover(pop[i + 1]))
        i += 2
    return best, pop


if __name__ == '__main__':
    if len(sys.argv) != 5:
        print('usage: %s min_key_size max_key_size path nb_turn' % sys.argv[0])
        sys.exit(1)
    min_key = int(sys.argv[1])
    max_key = int(sys.argv[2])
    path = sys.argv[3]
    nb_turn = int(sys.argv[4])
    with open(path) as f:
        cipher = f.read().lower()
    pop = [Individual(random.randint(min_key, max_key), cipher, mutation_rate=0.4) for _ in range(400)]
    for i in range(nb_turn):
        best, pop = next(pop)
        os.system('clear')
        print('Generation: %d' % i)
        print('Best individual: %s' % best)
        print(crypt.decrypt(best.genome, best._cipher))

