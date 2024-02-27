from batistic_ilario_vj6_helper_functions import read_file_csv, total_distance, get_path_to_all_cities
from itertools import permutations
from time import time

def brute_force(file_dict: dict):
    cities = list(file_dict.keys())
    shortest_distance, shortest_path = None, None
    
    for permutation in permutations(cities):
        total = total_distance(permutation, file_dict)
        if shortest_distance is None:
            shortest_distance = total
            shortest_path = permutation
        elif shortest_distance > total:
            shortest_distance = total
            shortest_path = permutation
    
    return shortest_path, shortest_distance

def zadatak1():
    file_dict = read_file_csv('distance_smaller_set.csv')
    start = time()
    shortest_path, shortest_distance = brute_force(file_dict)
    end = time()
    taken_path = get_path_to_all_cities(shortest_path, file_dict)
    print("\n\nBrute force algorithm: \n\n")
    print(f"Shortest path: {shortest_path} and shortest distance: {shortest_distance}")
    print(f"Shortest taken path: {taken_path}")
    print(f"Total elasped time: {end - start}")