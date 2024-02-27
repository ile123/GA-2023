from batistic_ilario_vj6_helper_functions import read_file_csv, generate_edges_from_file_dict
from time import time

def has_no_cycle(graph, start, visited):
    stack = {(start, None)}
    while stack:
        current, parent = stack.pop()
        visited.add(current)
        for neighbor in graph.get(current, []):
            if neighbor not in visited:
                stack.add((neighbor, current))
            elif neighbor != parent:
                return True
    return False

def sorted_edges(edges):
    edges.sort(key=lambda x: x[2])
    graph = {}
    visited = set()
    for edge in edges:
        start_edge_degree = sum(neighbor not in visited for neighbor in graph.get(edge[0], []))
        if not start_edge_degree >= 3 and not has_no_cycle(graph, edge[0], visited):
            if edge[0] not in graph:
                graph[edge[0]] = [(edge[1], edge[2])]
            else:
                graph[edge[0]].append((edge[1], edge[2]))
            visited.add(edge[0])
            visited.add(edge[1])
    return graph


def zadatak3():
    file_dict = read_file_csv('distance.csv')
    edges = generate_edges_from_file_dict(file_dict)
    edges.sort(key= lambda x: x[2])
    start = time()
    graph = sorted_edges(edges)
    end = time()
    print("\n\nSorted neighboors: \n\n")
    print(f"Graph: {graph}")
    print(f"Execution time: {end - start}")    