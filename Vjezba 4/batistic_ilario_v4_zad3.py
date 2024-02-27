from helper_functions import get_graph_information
from Graph import Graph

def dfs(graph: dict, start: int, visited: set):
    visited.add(start)
    for node in graph.get(start, []):
        if node not in visited:
            dfs(graph, node, visited)


def is_connected(graph: dict):
    start = next(iter(graph))
    visited = set()
    dfs(graph, start, visited)
    return len(visited) == len(graph)

def is_euler(graph: Graph):
    if not is_connected(graph.matrices['Graph Neighborhood Matrix']):
        return False
    odd_counter = 0
    for i in graph.matrices['Graph Neighborhood Matrix'].values():
        if len(i) % 2 != 0:
            odd_counter += 1
    if odd_counter == 0 or odd_counter > 2:
        return True
    else:
        return False


def zadatak_3():
    graph = get_graph_information("graph.txt")
    print(f"Is graph euler: {is_euler(graph)}")