from utils import getCost, numberOfCitiesVisited
from random import randint
from random_method import RandomMethod
import math

class GreedyRandomOptimization:
    
    def __init__(self, edges):
        self.edges = edges
        self.numberOfCities = len(edges)

    def run(self, inputTour, inputCost, maxTries):
        stop = False
        bestTour = inputTour.copy()
        bestCost = inputCost
        oldTour = inputTour.copy()
        oldCost = inputCost
        sameCost = 0
        
        propabiltyOfAcceptance = 0.9
        
        while True: 
            for counter in range(0, maxTries):
                index1 = randint(0, self.numberOfCities - 1)
                index2 = randint(0, self.numberOfCities - 1)
                city1 = oldTour[index1]
                city2 = oldTour[index2]
                tempTour = oldTour.copy()
                tempTour[index1] = city2
                tempTour[index2] = city1
                tempCost = getCost(tempTour, self.edges)

                if tempCost < oldCost:
                    oldTour = tempTour
                    oldCost = tempCost
                
                    if tempCost < bestCost:
                        bestCost = tempCost
                        bestTour = tempTour
                else:
                    rnd = (randint(0, 101)/ 100)
                    if(rnd < propabiltyOfAcceptance):
                        oldCost = tempCost
                        oldTour = tempTour
            
            propabiltyOfAcceptance = 0.9 * propabiltyOfAcceptance
            if propabiltyOfAcceptance < 0.0000001:
                break
        
        return bestTour, bestCost


    
    
    

