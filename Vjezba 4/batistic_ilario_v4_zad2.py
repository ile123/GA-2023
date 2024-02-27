from helper_functions import get_graph_information
from Graph import Graph

def number_of_vertices(graph: Graph):
    return graph.vertices

def number_of_edges(graph: Graph):
    return len(graph.edges)

def degre_of_each_vertice(graph: Graph):
    vertices = [int(i) for i in list(graph.labels.keys())]
    degre_of_each_vertice = []
    for vertice in vertices:
        counter = 0
        for edge in graph.edges:
            if vertice in edge:
                counter += 1
        degre_of_each_vertice.append((vertice, counter))
        counter = 0
    return degre_of_each_vertice

def vertices_with_max_degre(graph: Graph):
    max_degre = 0
    vertice_array = []
    degres_of_all_vertices = degre_of_each_vertice(graph)
    for item in degres_of_all_vertices:
        if item[1] > max_degre:
            max_degre = item[1]
            vertice_array = [item[0]]
        elif item[1] == max_degre:
            vertice_array.append(item[0])
    return vertice_array

def zadatak_2():
    graph = get_graph_information("graph.txt")
    print(graph)
    print(f"Vertices: {number_of_vertices(graph)}")
    print(f"Edges: {number_of_edges(graph)}")
    print(f"Degre of each vertice: {degre_of_each_vertice(graph)}")
    print(f"Vertices with max degre: {vertices_with_max_degre(graph)}")
