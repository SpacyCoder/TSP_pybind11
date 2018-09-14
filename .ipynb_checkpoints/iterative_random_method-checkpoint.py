from utils import getCost, numberOfCitiesVisited
from random import randint
from random_method import RandomMethod
import math

class IterativeRandomMethod:
    
    def __init__(self, edges, maxIterations):
        self.edges = edges
        self.numberOfCities = len(edges)
        self.maxIterations = maxIterations

    def isBestTour(self, tour):
        
        newCost = getCost(tour, self.edges)
        return newCost < bestCost, newCost
        
    def run(self):
        stop = False
        iterations = 0
        bestTour = []
        bestCost =  math.inf
        
        while not stop:
            tour, cost = RandomMethod(self.edges).run()
            isBest = cost < bestCost
            if isBest:
                bestTour = tour
                bestCost = cost
            iterations += 1
            stop =  iterations >= self.maxIterations
        
        return bestTour, bestCost


    
    
    