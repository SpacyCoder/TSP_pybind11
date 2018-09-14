from utils import getCost, numberOfCitiesVisited
from random import randint
from random_method import RandomMethod
import math

class GreedyOptimization:
    
    def __init__(self, edges, stopCriterion):
        self.edges = edges
        self.numberOfCities = len(edges)
        self.stopCriterion = stopCriterion
    
    def run(self, inputTour):
        tour = inputTour.copy()
        stop = False
        bestCost = math.inf
        sameCost = 0

        while not stop:
            index1 = randint(0, self.numberOfCities - 1)
            index2 = randint(0, self.numberOfCities - 1)
            city1 = tour[index1]
            city2 = tour[index2]
            tempTour = tour.copy()
            tempTour[index1] = city2
            tempTour[index2] = city1
            tempCost = getCost(tempTour, self.edges)

            if tempCost <= bestCost:
                tour = tempTour
                bestCost = tempCost
            
                if(tempCost == bestCost):
                    sameCost += 1
                else:
                    sameCost = 0
            
            stop = sameCost >= self.stopCriterion
            
            
        
        return tour, getCost(tour, self.edges)


    
    
    