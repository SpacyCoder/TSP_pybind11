
def getCost(selectedTour, edges):
    cost = 0
    for city in range(1, len(selectedTour)):
        fromCity = selectedTour[city - 1]
        toCity = selectedTour[city]
        cost += edges[fromCity][toCity]
    return cost

def numberOfCitiesVisited(visitedCities):
    count = 0
    for visited in visitedCities:
        if visited:
            count += 1
    return count