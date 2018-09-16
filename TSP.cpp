#include <pybind11/pybind11.h>
#include <pybind11/stl.h>
#include <vector>
#include <random>
#include <iostream>
#include <limits>
#include <cmath>

struct RetVal {
  std::vector<int> tour;
  int cost;
};

int dist(int x1, int y1, int x2, int y2) {
    int delta_x = x2 - x1;
    int delta_y = y2 - y1;

    return std::round(std::sqrt((delta_x * delta_x)  + (delta_y* delta_y)));
}

std::vector<std::vector<int>> generate_edges(std::vector<int> x, std::vector<int> y, int length) {
    std::vector<std::vector<int>> edges;

    for (int i = 0; i < length; i++) {
        std::vector<int> row;
        for(int j = 0; j < length; j++) {
            int x1 = x[i];
            int y1 = y[i];
            int x2 = x[j];
            int y2 = y[j];
            row.push_back(dist(x1, y1, x2, y2));
        }
        edges.push_back(row);
    }

    return edges;
}

int get_cost(std::vector<int> tour, int length, std::vector<std::vector<int>> edges){
    int cost = 0;
    for (int i = 0; i < length; i++) {
        int fromCity = tour[i - 1];
        int toCity = tour[i];
        cost += edges[fromCity][toCity];
    }
    return cost;
}

int num_cities_visited(bool visited_cities[], int length, std::vector<std::vector<int>> edges) {
    int count = 0;
    for(int i = 0; i < length; i++ ) {
        if(visited_cities[i]) {
            count++;
        }
    }
    return count;
}


std::tuple<std::vector<int>, int> random_method(std::vector<std::vector<int>> edges, int num_cities) {
    bool visited_cities[num_cities] = {false};
    std::vector<int> tour;

    std::random_device rdev;
    std::mt19937 rgen(rdev());
    std::uniform_int_distribution<int> idist(0, num_cities - 1); 
    
    int starting_city = idist(rgen);
    tour.push_back(starting_city);
    visited_cities[starting_city] = true;
    
    int tour_length = 1;
    while (tour_length != num_cities) {
        int rand_index = idist(rgen);
        if(!visited_cities[rand_index]) {
            tour_length++;
            visited_cities[rand_index] = true;
            tour.push_back(rand_index);
        }
    }

    return std::make_tuple(tour, get_cost(tour, num_cities, edges));
}
/*
bool isBestTour(std::vector<int> tour, int length, std::vector<std::vector<int>> edges, int best_cost) {
    int new_cost = get_cost(tour, length, edges);
    return new_cost < best_cost, newCnew_costost
}
*/

std::tuple<std::vector<int>, int> iterative_random_method(std::vector<std::vector<int>> edges, int num_cities, int max_iterations){
    bool stop = false;
    int iterations = 0;
    std::vector<int> best_tour;
    int best_cost = std::numeric_limits<int>::max();
        
    while (!stop) {
        std::vector<int> new_tour;
        int new_cost;
        std::tie(new_tour, new_cost) = random_method(edges, num_cities);
        bool is_best = new_cost < best_cost;
        if (is_best) {
            best_tour = new_tour;
            best_cost = new_cost;
        }
        iterations++;
        stop =  iterations >= max_iterations;
    }
    return std::make_tuple(best_tour, best_cost);
}

int get_nearest_city(bool visited_cities[], int length, std::vector<int> city_dist) {
    int smallest_cost = std::numeric_limits<int>::max();
    int to_city = 0;

    for(int city = 0; city < length; city++) {
        const int cost = city_dist[city];
        if(cost == 0 || visited_cities[city]) {
            continue;
        } 
        if(cost < smallest_cost) {
            to_city = city;
            smallest_cost = cost;
        }
    }
    return to_city;
}

std::tuple<std::vector<int>, int> greedy_method(std::vector<std::vector<int>> edges, int num_cities){
    bool visited_cities[num_cities] = {false};
    std::vector<int> tour;

    std::random_device rdev;
    std::mt19937 rgen(rdev());
    std::uniform_int_distribution<int> idist(0, num_cities - 1); 
    
    int starting_city = idist(rgen);
    tour.push_back(starting_city);
    visited_cities[starting_city] = true;

    int current_city = starting_city;
    int tour_length = 1;
    while (tour_length < num_cities) {
        int city = get_nearest_city(visited_cities, num_cities, edges[current_city]);
        current_city = city;
        visited_cities[city] = true;
        tour.push_back(city);
        tour_length++;
    }

    return std::make_tuple(tour, get_cost(tour, num_cities, edges));
}


std::tuple<std::vector<int>, int> greedy_optimization(std::vector<int> tour, int cost, std::vector<std::vector<int>> edges, int num_cities, int stop_criterion) {
    std::random_device rdev;
    std::mt19937 rgen(rdev());
    std::uniform_int_distribution<int> idist(0, num_cities - 1); 
    std::vector<int> best_tour = tour;
    bool stop = false;
    int best_cost = cost;
    int not_changed_count = 0;

    while (!stop) {
        const int index1 = idist(rgen);
        const int index2 = idist(rgen);
        const int city1 = best_tour[index1];
        const int city2 = best_tour[index2];
        std::vector<int> temp_tour = best_tour;

        temp_tour[index1] = city2;
        temp_tour[index2] = city1;

        const int temp_cost = get_cost(temp_tour, num_cities, edges);
        
        if (temp_cost < best_cost) {
            best_tour = temp_tour;
            best_cost = temp_cost;
            not_changed_count = 0;
        } else {
            not_changed_count++;
        }
        stop = not_changed_count >= stop_criterion;
    }

    return std::make_tuple(best_tour, best_cost);
}

std::tuple<std::vector<int>, int> greedy_random_optimization(std::vector<int> tour, int cost, std::vector<std::vector<int>> edges, int num_cities, int max_tries) {
    std::random_device rdev;
    std::mt19937 rgen(rdev());
    std::uniform_int_distribution<int> idist(0, num_cities - 1); 
    std::uniform_real_distribution<double> rdist(0, 1);
    std::vector<int> best_tour = tour;
    int best_cost = cost;
    std::vector<int> old_tour = best_tour;
    int old_cost = best_cost;
    double propabilty_of_acceptance = 0.9;

    do {
        for(int i = 0; i < max_tries; i++) {
            const int index1 = idist(rgen);
            const int index2 = idist(rgen);
            const int city1 = old_tour[index1];
            const int city2 = old_tour[index2];
            std::vector<int> temp_tour = old_tour;
            temp_tour[index1] = city2;
            temp_tour[index2] = city1;
            const int temp_cost = get_cost(temp_tour, num_cities, edges);

            if (temp_cost < old_cost) {
                old_cost = temp_cost;
                old_tour = temp_tour;

                if (temp_cost < best_cost) {
                    best_cost = temp_cost;
                    best_tour = temp_tour;
                }
            } else {
                double rnd = rdist(rgen);
                if(rnd < propabilty_of_acceptance) {
                    old_cost = temp_cost;
                    old_tour = temp_tour;
                }
            }
        }
        propabilty_of_acceptance = 0.9 * propabilty_of_acceptance;
    } while(propabilty_of_acceptance > 0.0000001);

    return std::make_tuple(best_tour, best_cost);
}

    
PYBIND11_MODULE(TSP, m) {
    m.doc() = "pybind11 plugin";
    m.def("random_method", &random_method, "Finds a random solution to the traveling salesman problem");
    m.def("iterative_random_method", &iterative_random_method, "Finds a solution to the traveling salesman problem");
    m.def("greedy_method", &greedy_method, "Finds a solution to the traveling salesman problem");

    m.def("greedy_optimization", &greedy_optimization, "Optimizes a solution to TSP");
    m.def("greedy_random_optimization", &greedy_random_optimization, "Optimizes a solution to TSP");
    m.def("generate_edges", &generate_edges, "Generates edges weights from  input coordiantes");
}