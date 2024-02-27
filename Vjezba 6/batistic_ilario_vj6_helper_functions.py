import csv
from collections import deque

def read_file_csv(file_path):
    main_dict = {}
    temp_key = ""
    with open(file_path, "r") as csvfile:
        file = csv.DictReader(csvfile)
        for line in file:
            for key, value in line.items():
                if key == '':
                    main_dict[value] = {}
                    temp_key = value
                elif temp_key != key:
                    main_dict[temp_key][key] = value
    return main_dict

def print_file_dict(file_dict: dict):
    for key, value in file_dict.items():
        print(f"City: {key}\n\nNeighboors: \n\n{value}\n\n\n")

def total_distance(path, distances):
    total_distance = 0
    for i in range(len(path) - 1):
        total_distance += int(distances[path[i]][path[i + 1]])
    return total_distance

def get_path_to_all_cities(path, distances):
    path_details = []
    total_distance = 0
    for i in range(len(path) - 1):
        total_distance += int(distances[path[i]][path[i + 1]])
        path_details.append((path[i], path[i + 1], int(distances[path[i]][path[i + 1]]), total_distance))
    return path_details

def generate_adjencacy_matrix(file_dict: dict):
    cities = sorted(list(file_dict.keys()))
    adjacency_matrix = [[0 for _ in range(len(cities))] for _ in range(len(cities))]
    for i in range(len(cities)):
        for j in range(len(cities)):
            if i != j:
                from_city = cities[i]
                to_city = cities[j]
                distance = file_dict.get(from_city, {}).get(to_city)
                if distance:
                    adjacency_matrix[i][j] = int(distance)
    return cities, adjacency_matrix

def generate_edges_from_file_dict(file_dict: dict):
    edges = []
    city_dict = {}
    for index, city in enumerate(file_dict):
        city_dict[city] = index
    for key, values in file_dict.items():
        for neighboor in values:
            edges.append((city_dict[key], city_dict[neighboor], int(values[neighboor])))
    return edges