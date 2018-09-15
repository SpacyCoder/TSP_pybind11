from random import randint
from utils import getCost, numberOfCitiesVisited
from random_method import RandomMethod
from iterative_random_method import IterativeRandomMethod
from greedy_method import GreedyMethod
from greedy_optimization import GreedyOptimization
from greedy_random_optimization import GreedyRandomOptimization
import numpy as np
import time

import random, numpy
edges = numpy.random.randint(1,1000,(1000, 1000))
numberOfCities = len(edges)
for i in range(0, len(edges)):
    edges[i][i] = 0


print("Start Random Algorithm")
start = time.time()
randomTour, randomCost = RandomMethod(edges).run()
end = time.time()
print("Random used:",end-start, "seconds")
print("Random Cost:", randomCost)

iterations = 10
print("Start Iterative Random Algorithm")
start = time.time()
iterativeRandomTour, iterativeRandomCost = IterativeRandomMethod(edges, iterations).run()
end = time.time()
print("Iterative Random used:",end-start, "seconds")
print("Iterative Random Cost:", iterativeRandomCost)

print("Start Greedy Algorithm")
start = time.time()
greedyTour, greedyCost = GreedyMethod(edges).run()
end = time.time()
print("Greedy used:",end-start, "seconds")
print( "Greedy Cost:", greedyCost)

stopCriterion = 20
greedyOptimized, greedyOptimizedCost = GreedyOptimization(edges, stopCriterion).run(randomTour)
print( "Random Cost(Greedy optimized):", greedyOptimizedCost)

greedyOptimized, greedyOptimizedCost = GreedyOptimization(edges, stopCriterion).run(iterativeRandomTour)
print("Iterative Random Cost(Greedy optimized):", greedyOptimizedCost)

greedyOptimized, greedyOptimizedCost = GreedyOptimization(edges, stopCriterion).run(greedyTour)
print("Greedy Cost(Greedy optimized):", greedyOptimizedCost)

maxTries = 20
greedyRandomOptimized, greedyRandomOptimizedCost = GreedyRandomOptimization(edges).run(randomTour, randomCost, maxTries)
print("Random Cost(Greedy Random optimized):", greedyRandomOptimizedCost)

greedyRandomOptimized, greedyRandomOptimizedCost = GreedyRandomOptimization(edges).run(iterativeRandomTour, iterativeRandomCost, maxTries)
print("Iterative Random Cost(Greedy Random optimized):", greedyRandomOptimizedCost)

greedyRandomOptimized, greedyRandomOptimizedCost = GreedyRandomOptimization(edges).run(greedyTour, greedyCost, maxTries)
print("Greedy Cost(Greedy Random optimized):", greedyRandomOptimizedCost)
