import random
import numpy as np
import TSP
import time
import pandas as pd
import math

def dist(x1, y1,x2, y2):
    delta_x = x2 - x1
    delta_y = y2 - y1
    return int(math.floor(math.sqrt(delta_x**2  + delta_y**2)))

def make_matrix(x, y):
    length = len(x)
    D = np.empty(shape=(length, length))
    for i in range(length - 1):
        for j in range(length - 1):
            x1 = x[i]
            y1 = y[i]
            x2 = x[j]
            y2 = y[j]
            D[i][j] = dist(x1, y1, x2, y2)
    return D

num_cities = 1000
x = np.random.randint(0, 10000, size=num_cities)
y = np.random.randint(0, 10000, size=num_cities)

edges = TSP.generate_edges(x, y, len(x))

for i in range(0, num_cities):
    edges[i][i] = 0

greedy_stop_criterion = 200
random_greedy_max_tries = 200
# RANDOM METHOD
loops = 1000

print("Starting random method...")
sum_random = 0
min = math.inf
max = 0
for i in range(loops):
    start = time.time()
    random_tour, random_cost = TSP.random_method(edges, num_cities)
    end = time.time()
    random_time = end - start
    sum_random += random_time
    min = random_time if random_time < min else min
    max = random_time if random_time > max else max

print("Max:", max, "Min", min, "Average:", sum_random/loops)
print("Random Cost:", random_cost)

print("Start optimizing")
sum_random_optimized = 0
min = math.inf
max = 0
for i in range(loops):
    start = time.time()
    random_tour, random_cost = TSP.random_method(edges, num_cities)
    greedy_optimized_tour, greedy_optimized_cost = TSP.greedy_optimization(random_tour, random_cost, edges, num_cities, greedy_stop_criterion)
    end = time.time()
    runtime = end - start
    sum_random_optimized += runtime
    min = runtime if runtime < min else min
    max = runtime if runtime > max else max

print("Max:", max, "Min", min, "Average:", sum_random_optimized/loops)
print("Random Cost(Greedy_optimized):", greedy_optimized_cost)

print("Start random optimizing")
sum_random_optimized_rand = 0
min = math.inf
max = 0
for i in range(loops):
    start = time.time()
    random_tour, random_cost = TSP.random_method(edges, num_cities)
    greedy_random_optimized_tour, greedy_random_optimized_cost = TSP.greedy_random_optimization(random_tour, random_cost, edges, num_cities, random_greedy_max_tries)
    end = time.time()
    runtime = end - start
    sum_random_optimized_rand += runtime
    min = runtime if runtime < min else min
    max = runtime if runtime > max else max

print("Max:", max, "Min", min, "Average:", sum_random_optimized_rand/loops)
print("Random Cost(Greedy Random Optimized):", greedy_random_optimized_cost)
print('----------------------------')


print("Starting iterative method...")
max_iterations = 100
sum_iter = 0
min = math.inf
max = 0
for i in range(loops):
    start = time.time()
    iterative_random_tour, iterative_random_cost = TSP.iterative_random_method(edges, num_cities, max_iterations)
    end = time.time()
    runtime = end - start
    sum_iter += runtime
    min = runtime if runtime < min else min
    max = runtime if runtime > max else max

print("Max:", max, "Min", min, "Average:", sum_iter/loops)
print("Iterative Random Cost:", iterative_random_cost)

print("Start optimizing")
sum_iter_optimized = 0
min = math.inf
max = 0
for i in range(loops):
    start = time.time()
    iterative_random_tour, iterative_random_cost = TSP.iterative_random_method(edges, num_cities, max_iterations)
    greedy_optimized_tour, greedy_optimized_cost = TSP.greedy_optimization(iterative_random_tour, iterative_random_cost, edges, num_cities, greedy_stop_criterion)
    end = time.time()
    runtime = end - start
    sum_iter_optimized += runtime
    min = runtime if runtime < min else min
    max = runtime if runtime > max else max

print("Max:", max, "Min", min, "Average:", sum_iter_optimized/loops)
print("Iter Cost(Greedy_optimized):", greedy_optimized_cost)

sum_iter_rand_optimized = 0
min = math.inf
max = 0
for i in range(loops):
    start = time.time()
    iterative_random_tour, iterative_random_cost = TSP.iterative_random_method(edges, num_cities, max_iterations)
    greedy_random_optimized_tour, greedy_random_optimized_cost = TSP.greedy_random_optimization(iterative_random_tour, iterative_random_cost, edges, num_cities, random_greedy_max_tries)
    end = time.time()
    runtime = end - start
    sum_iter_rand_optimized += runtime
    min = runtime if runtime < min else min
    max = runtime if runtime > max else max

print("Max:", max, "Min", min, "Average:", sum_iter_rand_optimized/loops)
print("Iter Cost(Greedy rand optimized):", greedy_optimized_cost)

print('------------------------------')

print("Starting Greedy method...")
sum_greedy = 0
min = math.inf
max = 0
for i in range(loops):
    start = time.time()
    greedy_tour, greedy_cost = TSP.greedy_method(edges, num_cities)
    end = time.time()
    runtime = end - start
    sum_greedy += runtime
    min = runtime if runtime < min else min
    max = runtime if runtime > max else max

print("Max:", max, "Min", min, "Average:", sum_greedy/loops)
print("Greedy Cost:", greedy_cost)


print("Start opimizing method...")
sum_greedy_opti = 0
min = math.inf
max = 0
for i in range(loops):
    start = time.time()
    greedy_tour, greedy_cost = TSP.greedy_method(edges, num_cities)
    greedy_optimized_tour, greedy_optimized_cost = TSP.greedy_optimization(greedy_tour, greedy_cost, edges, num_cities, greedy_stop_criterion)
    end = time.time()
    runtime = end - start
    sum_greedy_opti += runtime
    min = runtime if runtime < min else min
    max = runtime if runtime > max else max

print("Max:", max, "Min", min, "Average:", sum_greedy_opti/loops)
print("Greedy Cost:", greedy_cost)

sum_greedy_opti_rand = 0
min = math.inf
max = 0
for i in range(loops):
    start = time.time()
    greedy_tour, greedy_cost = TSP.greedy_method(edges, num_cities)
    greedy_random_optimized_tour, greedy_random_optimized_cost = TSP.greedy_random_optimization(greedy_tour, greedy_cost, edges, num_cities, random_greedy_max_tries)
    end = time.time()
    runtime = end - start
    sum_greedy_opti_rand += runtime
    min = runtime if runtime < min else min
    max = runtime if runtime > max else max

print("Max:", max, "Min", min, "Average:", sum_greedy_opti_rand/loops)
print("Greedy Cost(Greedy Random Optimized):", greedy_random_optimized_cost)

