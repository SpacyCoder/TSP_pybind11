from utils import getCost, numberOfCitiesVisited
from random import randint
from random_method import RandomMethod
import math

class GreedyMethod:
    
    def __init__(self, edges):
        self.edges = edges
        self.numberOfCities = len(edges)

    def isBestTour(self, tour):
        newCost = getCost(tour, self.edges)
        return newCost < bestCost, newCost
    
    def getNearestCity(self, fromCity, visitedCities):
        smallestCost = math.inf
        toCity = 0
        for city, cost in enumerate(self.edges[fromCity]):
            if city == fromCity: 
                continue
            if cost < smallestCost and not visitedCities[city]:
                smallestCost = cost
                toCity = city
        return toCity
        
    def run(self):
        visitedCities = [False] * self.numberOfCities
        tour = []
        startingCity = randint(0, self.numberOfCities - 1)
        visitedCities[startingCity] = True
        tour.append(startingCity)
        currentIndex = 0
        while numberOfCitiesVisited(visitedCities) != self.numberOfCities:
            city = self.getNearestCity(tour[currentIndex], visitedCities)
            currentIndex += 1
            visitedCities[city] = True
            tour.append(city)
        
        return tour, getCost(tour, self.edges)


    
    
    