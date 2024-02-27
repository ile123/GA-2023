from batistic_ilario_v5_helper_functions import get_graph_information

"""
def kosaraju_algorithm(arcs, starting_vertex, vertices):
    visited = set()
    vertex = None
    to_visit = [starting_vertex]
    stack = set()
    number_of_components, component_size_counter, bigest_component = 0, 0, []
    while len(visited) < vertices:
        previous_vertex = to_visit[1] if len(to_visit) > 1 else to_visit[0]
        vertex = to_visit.pop(0)
        if starting_vertex in to_visit:
            number_of_components += 1
            stack.add(vertex)
            bigest_component.append(component_size_counter)
            component_size_counter = 0
            vertex = previous_vertex
        if vertex not in visited:
            component_size_counter += 1
            visited.add(vertex)
            to_visit = [arc[1] for arc in get_all_arcs_with_vertex(vertex, arcs)]
    bigest_component.sort()
    return number_of_components, bigest_component[-1]

def get_all_arcs_with_vertex(vertex, arcs):
    return [arc for arc in arcs if vertex == arc[0]]
"""

def dfs(graph, start, visited, stack):
        visited.add(start)
        for arc in graph:
            if arc[0] == start and arc[1] not in visited:
                dfs(graph, arc[1], visited, stack)
        stack.append(start)

def dfs_for_reversed_graph(graph, start, visited, component):
        visited.add(start)
        component.append(start)
        for arc in graph:
            if arc[1] == start and arc[0] not in visited:
                dfs_for_reversed_graph(graph, arc[0], visited, component)

def reverse_graph(arcs):
    return [(arc[1], arc[0]) for arc in arcs]

def kosaraju_algorithm(arcs, vertices):
    visited = set()
    stack = []
    for vertex in range(vertices):
        if vertex not in visited:
            dfs(arcs, vertex, visited, stack)
    reversed_graph = reverse_graph(arcs)
    visited.clear()
    components = []
    while stack:
        vertex = stack.pop()
        if vertex not in visited:
            component = []
            dfs_for_reversed_graph(reversed_graph, vertex, visited, component)
            components.append(component)
    size_of_biggest_component = max([len(component) for component in components])
    return len(components), size_of_biggest_component

def zadatak_2():
    graph = get_graph_information("football.net")
    number_of_components, biggest_component = kosaraju_algorithm(graph.arcs, graph.vertices)
    print(f"Number of components and the size of the biggest component: {number_of_components} and {biggest_component}")