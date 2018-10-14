# TSP + pybind

TSP implemented with pybind11

## Dependencies
pybind11: https://pybind11.readthedocs.io/en/master/index.html

## Installation 
1. Clone repository
2. Compile with the following command: c++ -O3 -Wall -shared -std=c++11 -fPIC `python3 -m pybind11 --includes` main.cpp -o main`python3-config --extension-suffix`
3. Run: python compare.py
