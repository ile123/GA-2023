from helper_functions import get_graph_information, neighborhood_to_edges, incidence_to_edges, adjacency_to_edges, last_vertice

def neighborhood_to_incidence(neighborhood_matrix: dict):
    incidence_matrix = []
    edges = neighborhood_to_edges(neighborhood_matrix)
    vertice = max([max(item) for item in edges])
    for _ in range(0, vertice):
        incidence_matrix.append([0] * len(edges))
    for index, (v1, v2) in enumerate(edges):
        incidence_matrix[v1 - 1][index] = 1
        incidence_matrix[v2 - 1][index] = 1
    return incidence_matrix

def neighborhood_to_adjencacy(neighborhood_matrix: dict):
    adjacency_matrix = []
    last_vertice = 0
    for i in neighborhood_matrix.values():
        if max(i) > last_vertice:
            last_vertice = max(i)
    for _ in range(0, 5):
        adjacency_matrix.append([0] * last_vertice)
    for v1 in neighborhood_matrix:
        for v2 in neighborhood_matrix[v1]:
            adjacency_matrix[int(v1) - 1][v2 - 1] = 1
            adjacency_matrix[v2 - 1][int(v1) - 1] = 1
    return adjacency_matrix


def adjencacy_to_neighborhood(adjencacy_matrix: dict):
    neighboorhood_matrix = {}
    edges = adjacency_to_edges(adjencacy_matrix)
    for i, j in edges:
        if i not in neighboorhood_matrix:
            neighboorhood_matrix[i] = [j]
        else:
            neighboorhood_matrix[i].append(j)
    for i in neighboorhood_matrix.values():
        i.sort()
    return neighboorhood_matrix


def adjencacy_to_incidence(adjencacy_matrix: dict):
    incidence_matrix = []
    edges = adjacency_to_edges(adjencacy_matrix)
    vertices = last_vertice(edges)
    for _ in range(0, vertices):
        incidence_matrix.append([0] * len(edges))
    for index, (v1, v2) in enumerate(edges):
        incidence_matrix[v1 - 1][index] = 1
        incidence_matrix[v2 - 1][index] = 1
    return incidence_matrix



def incidence_to_neighborhood(incidence_matrix: dict):
    edges = incidence_to_edges(incidence_matrix)
    neighboorhood_matrix = {}
    for i, j in edges:
        if i not in neighboorhood_matrix:
            neighboorhood_matrix[i] = [j]
        else:
            neighboorhood_matrix[i].append(j)
    for i in neighboorhood_matrix.values():
        i.sort()
    return neighboorhood_matrix


def incidence_to_adjacency(incidence_matrix):
    adjacency_matrix = [[0] * len(incidence_matrix) for _ in range(len(incidence_matrix))]
    edges = incidence_to_edges(incidence_matrix)
    for v1, v2 in edges:
        adjacency_matrix[v1 - 1][v2 - 1] = 1
        adjacency_matrix[v2 - 1][v1 - 1] = 1
    return adjacency_matrix


def zadatak_1():
    graph = get_graph_information('graph.txt')
    print(graph)
    #print(neighborhood_to_adjencacy(graph.matrices['Graph Neighborhood Matrix']))
    #print(neighborhood_to_incidence(graph.matrices['Graph Neighborhood Matrix']))
    #print(adjencacy_to_neighborhood(graph.matrices['Adjacency Matrix']))
    #print(adjencacy_to_incidence(graph.matrices['Adjacency Matrix']))
    print(incidence_to_neighborhood(graph.matrices['Incidence Matrix']))
    print(incidence_to_adjacency(graph.matrices['Incidence Matrix']))
