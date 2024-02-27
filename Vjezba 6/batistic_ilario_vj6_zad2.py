from batistic_ilario_vj6_helper_functions import read_file_csv, generate_adjencacy_matrix
from time import time

def nearest_cities(adjencacy_matrix, cities):
    print(cities)
    total_distance = 0
    visited = []
    path = []
    current_city = 0
    visited.append(current_city)
    while len(visited) < len(adjencacy_matrix):
        nearest_city, min_distance = None, None
        for next_city in range(len(adjencacy_matrix)):
            if next_city not in visited and adjencacy_matrix[current_city][next_city] > 0:
                distance = adjencacy_matrix[current_city][next_city]
                if min_distance is None or distance < min_distance:
                    min_distance = distance
                    nearest_city = next_city
        visited.append(nearest_city)
        path.append((cities[current_city], cities[nearest_city], min_distance))
        total_distance += min_distance
        current_city = nearest_city
    return total_distance, path

def zadatak2():
    file_dict = read_file_csv("distance.csv")
    cities, adjencacy_matrix = generate_adjencacy_matrix(file_dict)
    start = time()
    total_distance, shortest_path = nearest_cities(adjencacy_matrix, cities)
    end = time()
    print("\n\nNearest neighboor algorithm: \n\n")
    print(f"Shortest path: {shortest_path} and total distance: {total_distance}")
    print(f"Total execution time: {end - start}")