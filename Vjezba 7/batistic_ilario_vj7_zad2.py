import networkx as nx
from batistic_ilario_vj7_helper_functions import loadGraph
from time import time
from queue import PriorityQueue

def greedy_bfs_algorithm(graph, start_node, destination_node):
    visited = set()
    path = []
    queue = PriorityQueue()
    queue.put((0, start_node, [start_node]))
    start = time()
    while queue:
        _, node, current_path = queue.get()
        if node not in visited:
            visited.add(node)
            if node == destination_node:
                path = current_path
                break
            for neighbor in graph.neighbors(node):
                if neighbor not in visited:
                    heuristic_cost = len(current_path)
                    new_path = current_path + [neighbor]
                    queue.put((heuristic_cost, neighbor, new_path))
    end = time()
    print(f"\n\nGreedy BFS: \n\nShortest path: {path}\n\nTime: {end - start}")


def a_star_algorithm(graph):
    start = time()
    shortest_path = nx.astar_path(graph, source='LHR', target='VIE', weight='weight')
    shortest_path_length = nx.astar_path_length(graph, source='LHR', target='VIE', weight='weight')
    end = time()
    print(f"\n\n*A: \n\nShortest path: {shortest_path}\n\nShortest path lenght: {shortest_path_length is None if 0 else shortest_path_length}\n\nTime: {end - start}")


def zad2():
    graph = loadGraph("gradovi-udaljenost.net")
    greedy_bfs_algorithm(graph, 'LHR', 'VIE')
    a_star_algorithm(graph)