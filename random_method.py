from utils import getCost, numberOfCitiesVisited
from random import randint

class RandomMethod:
    
    def __init__(self, edges):
        self.edges = edges
        self.numberOfCities = len(edges)
        
    def run(self):
        visitedCities = [False] * self.numberOfCities
        tour = []

        startingCity = randint(0, self.numberOfCities - 1)
        tour.append(startingCity)
        visitedCities[startingCity] = True

        while numberOfCitiesVisited(visitedCities) != self.numberOfCities:
            randomIndex = randint(0, self.numberOfCities - 1)
            if not visitedCities[randomIndex]:
                visitedCities[randomIndex] = True
                tour.append(randomIndex)
        
        return tour, getCost(tour, self.edges)
