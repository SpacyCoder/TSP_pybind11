import random, numpy
import TSP
import time


edges = numpy.random.randint(1, 50, (5000, 5000))
num_cities = len(edges)

for i in range(0, num_cities):
    edges[i][i] = 0

print("Starting random method...")
start = time.time()
random_tour, random_cost = TSP.random_method(edges, num_cities)
end = time.time()
print("Random Cost:", random_cost, "Time:", end-start)

max_iterations = 10
print("Starting iterative random method...")
start = time.time()
iterative_random_tour, iterative_random_cost = TSP.iterative_random_method(edges, num_cities, max_iterations)
end = time.time()
print("Iterative Random Cost:", iterative_random_cost, "Time:", end-start)

print("Starting greedy method...")
start = time.time()
greedy_tour, greedy_cost = TSP.greedy_method(edges, num_cities)
end = time.time()
print("Greedy Cost:", greedy_cost, "Time:", end-start)

print("------------------")
# OPTIMIZATION
stop_criterion = 2
greedy_optimized_tour, greedy_optimized_cost = TSP.greedy_optimization(random_tour, random_cost, edges, num_cities, stop_criterion)
print("Random Cost(Greedy_optimized):", greedy_optimized_cost)

greedy_optimized_tour, greedy_optimized_cost = TSP.greedy_optimization(iterative_random_tour, iterative_random_cost, edges, num_cities, stop_criterion)
print("Iterative Random Cost(Greedy Optimized):", greedy_optimized_cost)

greedy_optimized_tour, greedy_optimized_cost = TSP.greedy_optimization(greedy_tour, greedy_cost, edges, num_cities, stop_criterion)
print("Greedy Cost(Greedy Optimized):", greedy_optimized_cost)



max_tries = 10
greedy_random_optimized_tour, greedy_random_optimized_cost = TSP.greedy_random_optimization(random_tour, random_cost, edges, num_cities, max_tries)
print("Random Cost(Greedy Random Opimized):", greedy_random_optimized_cost)

greedy_random_optimized_tour, greedy_random_optimized_cost = TSP.greedy_random_optimization(iterative_random_tour, iterative_random_cost, edges, num_cities, max_tries)
print("Iterative Random Cost(Greedy Random Optimized):", greedy_random_optimized_cost)

greedy_random_optimized_tour, greedy_random_optimized_cost = TSP.greedy_random_optimization(greedy_tour, greedy_cost, edges, num_cities, max_tries)
print("Greedy Cost(Greedy Random Optimized):", greedy_random_optimized_cost)