from batistic_ilario_v5_helper_functions import get_graph_information
from collections import deque 

def print_algorithm_path(algorithm_name, used_arcs, labels):
    print(f"Name of the algorithm: {algorithm_name}\n")
    for arc in used_arcs:
        print(f"Vertices: {labels[str(arc[0])]} -> {labels[str(arc[1])]}\tWeight: {arc[2]}")
    print(f"\nTotal Amount: {len(used_arcs)}")


def does_not_form_an_circle(candidate_arc, arcs, used_arcs):
    visited = set()
    starting_point = candidate_arc[0]
    queue = deque([candidate_arc[0]])
    visited.add(candidate_arc[0])
    while queue:
        node = queue.popleft()
        all_arcs_by_vertice = [arc for arc in arcs if arc[0] == node]
        for arc in all_arcs_by_vertice:
            if arc in used_arcs:
                queue.append(arc[1])
            if arc[1] == starting_point:
                return False
    return True


def shortest_distance_by_vertex(arcs, used_arcs, vertex, visited):
    all_arcs_by_vertex = []
    viable_arcs = []
    for arc in arcs:
        if vertex == arc[0]:
            all_arcs_by_vertex.append(arc)
    for arc in all_arcs_by_vertex:
        if arc not in used_arcs and (arc[1], arc[0], arc[2]) not in used_arcs and arc[1] not in visited:
            viable_arcs.append(arc)
    viable_arcs.sort(key=lambda x: x[2])
    return viable_arcs[0] if len(viable_arcs) > 0 else None


def primov_algorithm(arcs: list, used_arcs: list, start: int, visited: set, vertices):
    unused_paths = []
    visited.add(start)
    if len(visited) == vertices:
        return
    for node in visited:
        path = shortest_distance_by_vertex(arcs, used_arcs, node, visited)
        if path is not None:
            unused_paths.append(path)
    unused_paths.sort(key=lambda x: x[2])
    used_arcs.append(unused_paths[0])
    primov_algorithm(arcs, used_arcs, used_arcs[-1][1], visited, vertices)


def get_all_arcs_with_vertex(vertex, arcs, used_arcs):
    return [arc for arc in arcs if vertex == arc[0] and arc not in used_arcs]


"""def get_all_arcs_with_v2(vertex, arcs, used_arcs):
    return [arc for arc in arcs if vertex == arc[1] and arc not in used_arcs]

def does_not_form_an_circle(arcs, used_arcs, v1, v2):
    v1_arcs = get_all_arcs_with_v1(v1, arcs, used_arcs)
    v2_arcs = get_all_arcs_with_v2(v2, arcs, used_arcs)
    for arc_v1 in v1_arcs:
        for arc_v2 in v2_arcs:
            if (arc_v1[1] == arc_v2[0]) and (arc_v2 not in used_arcs and arc_v1 not in used_arcs):
                return True
    return False"""


def kruskal_algorithm(arcs, used_arcs, visited, vertices):
    index = 0
    arcs.sort(key=lambda x: x[2])
    while len(used_arcs) < (vertices - 1):
        start, end, _ = arcs[index]
        if start not in visited or end not in visited:
            if start not in visited:
                if does_not_form_an_circle(arcs[index], arcs, used_arcs):
                    if (end, start, _) not in used_arcs:
                        used_arcs.append(arcs[index])
                    visited.add(start)
            elif end not in visited:
                if does_not_form_an_circle(arcs[index], arcs, used_arcs):
                    if (start, end, _) not in used_arcs:
                        used_arcs.append(arcs[index])
                    visited.add(end)
        elif does_not_form_an_circle(arcs[index], arcs, used_arcs):
            if (end, start, _) not in used_arcs:
                used_arcs.append(arcs[index])
        index += 1
    return used_arcs


def zadatak_1():
    graph = get_graph_information("airports-split.net")
    start = next(iter(graph.matrices['Graph Neighborhood Matrix']))
    visited = set()
    used_arcs = []
    primov_algorithm(graph.arcs, used_arcs, start, visited, graph.vertices)
    print(used_arcs)
    #print_algorithm_path("Primov", used_arcs, graph.labels)
    #kruskal_algorithm(graph.arcs, used_arcs, visited, graph.vertices)
    #print(graph)
    #print_algorithm_path("Kruskal", used_arcs, graph.labels)
