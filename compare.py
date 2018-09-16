import random
import numpy as np
import TSP
import time
import pandas as pd
import matplotlib.pyplot as plt
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

def make_plot(tour1, tour2, tour3):
    plot_x1 = []
    plot_y1 = []
    plot_x2 = []
    plot_y2 = []
    plot_x3 = []
    plot_y3 = []
    for i in range(len(tour1)):
        city_index1 = tour1[i]
        x_coord1 = x[city_index1]
        y_coord1 = y[city_index1]
        plot_x1.append(x_coord1)
        plot_y1.append(y_coord1)
        city_index2 = tour2[i]
        x_coord2 = x[city_index2]
        y_coord2 = y[city_index2]
        plot_x2.append(x_coord2)
        plot_y2.append(y_coord2)
        city_index3 = tour3[i]
        x_coord3 = x[city_index3]
        y_coord3 = y[city_index3]
        plot_x3.append(x_coord3)
        plot_y3.append(y_coord3)
    fig, ax = plt.subplots(3)

    ax[0].scatter(x, y, s=10, c='r')
    ax[0].plot(plot_x1, plot_y1)
    ax[1].scatter(x, y, s=10, c='r')
    ax[1].plot(plot_x2, plot_y2)
    ax[2].scatter(x, y, s=10, c='r')
    ax[2].plot(plot_x3, plot_y3)
    return fig, ax
    

num_cities = 50
x = np.random.randint(0, 10000, size=num_cities)
y = np.random.randint(0, 10000, size=num_cities)

edges = TSP.generate_edges(x, y, len(x))
fig, ax = plt.subplots()
ax.scatter(x, y, s=10, c='r')
ax.set_title('Cities')
ax.grid()

for i in range(0, num_cities):
    edges[i][i] = 0

greedy_stop_criterion = 100000
random_greedy_max_tries = 100000


# RANDOM METHOD
print("Starting random method...")
start = time.time()
random_tour, random_cost = TSP.random_method(edges, num_cities)
end = time.time()
random_time = end - start
print("Random Cost:", random_cost, "Time:", random_time)

start = time.time()
greedy_optimized_tour, greedy_optimized_cost = TSP.greedy_optimization(random_tour, random_cost, edges, num_cities, greedy_stop_criterion)
end = time.time()
greedy_optimized_random_time = end - start + random_time
print("Random Cost(Greedy_optimized):", greedy_optimized_cost)

start = time.time()
greedy_random_optimized_tour, greedy_random_optimized_cost = TSP.greedy_random_optimization(random_tour, random_cost, edges, num_cities, random_greedy_max_tries)
end = time.time()
random_random_optimized_time = (end-start) + random_time
print("Random Cost(Greedy Random Optimized):", greedy_random_optimized_cost)

fig, ax = make_plot(random_tour, greedy_optimized_tour, greedy_random_optimized_tour)
ax[0].set_title('Random Tour - cost: ' + str(random_cost) + ' - time: ' + str(random_time))
ax[1].set_title('Random Tour(Greedy Optimized)- cost: ' + str(greedy_optimized_cost) + ' - time: ' + str(greedy_optimized_random_time))
ax[2].set_title('Random Tour(Greedy Random Optimized)- cost: ' + str(greedy_random_optimized_cost) + ' - time: ' + str(random_random_optimized_time))

print('----------------------------')

## ITERATIVE RANDOM METHOD
max_iterations = 1000
print("Starting iterative random method...")
start = time.time()
iterative_random_tour, iterative_random_cost = TSP.iterative_random_method(edges, num_cities, max_iterations)
end = time.time()
iterative_time = end - start
print("Iterative Random Cost:", iterative_random_cost, "Time:", iterative_time)

start = time.time()
greedy_optimized_tour, greedy_optimized_cost = TSP.greedy_optimization(iterative_random_tour, iterative_random_cost, edges, num_cities, greedy_stop_criterion)
end = time.time()
greedy_iterative_time = end-start + iterative_time
print("Iterative Random Cost(Greedy Optimized):", greedy_optimized_cost)
start = time.time()
greedy_random_optimized_tour, greedy_random_optimized_cost = TSP.greedy_random_optimization(iterative_random_tour, iterative_random_cost, edges, num_cities, random_greedy_max_tries)
end = time.time()
iter_rand_random_optimized_time = (end-start) + iterative_time
print("Iterative Random Cost(Greedy Random Optimized):", greedy_random_optimized_cost)

fig, ax = make_plot(iterative_random_tour, greedy_optimized_tour, greedy_random_optimized_tour)
ax[0].set_title('Iterative Random Tour - cost: ' + str(iterative_random_cost) + ' - time: ' + str(iterative_time))
ax[1].set_title('Iterative Random Tour(Greedy Optimized) - cost: ' + str(greedy_optimized_cost) + ' - time: ' + str(greedy_iterative_time))
ax[2].set_title('Iterative Random Tour(Greedy Random Optimized)- cost: ' + str(greedy_random_optimized_cost) + ' - time: ' + str(iter_rand_random_optimized_time))

print('------------------------------')
## Greedy method
print("Starting greedy method...")
start = time.time()
greedy_tour, greedy_cost = TSP.greedy_method(edges, num_cities)
end = time.time()
greedy_time = end - start
print("Greedy Cost:", greedy_cost, "Time:", greedy_time)

start = time.time()
greedy_optimized_tour, greedy_optimized_cost = TSP.greedy_optimization(greedy_tour, greedy_cost, edges, num_cities, greedy_stop_criterion)
end = time.time()
greedy_optimized_time = end- start + greedy_time
print("Greedy Cost(Greedy Optimized):", greedy_optimized_cost)
start = time.time()
greedy_random_optimized_tour, greedy_random_optimized_cost = TSP.greedy_random_optimization(greedy_tour, greedy_cost, edges, num_cities, random_greedy_max_tries)
end = time.time()
greedy_rand_optimized_time = end - start + greedy_time
print("Greedy Cost(Greedy Random Optimized):", greedy_random_optimized_cost)

fig, ax = make_plot(greedy_tour, greedy_optimized_tour, greedy_random_optimized_tour)
ax[0].set_title('Greedy Tour - cost: ' + str(greedy_cost) + ' - time: ' + str(greedy_time))
ax[1].set_title('Greedy Tour(Greedy Optimized) - cost: ' + str(greedy_optimized_cost) + ' - time: ' + str(greedy_optimized_time))
ax[2].set_title('Greedy Tour(Greedy Random Optimized)- cost: ' + str(greedy_random_optimized_cost) + ' - time: ' + str(greedy_rand_optimized_time))



plt.show()
