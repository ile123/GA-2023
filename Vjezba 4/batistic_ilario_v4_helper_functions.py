from Graph import Graph

def get_index_of_file_part_in_list(list, part_of_file):
    for index, item in enumerate(list):
        if item[0] == part_of_file:
            return index
    return None


def read_and_cleane_file(file_path):
    file = open(file_path, "r").readlines()
    if not file:
        raise Exception("ERROR: File is either or empty or not found!")
    cleaned_file_list = []
    for line in file:
        string_line = line.replace("\n", "").split(" ")
        string_line = list(filter(lambda i: i != '', string_line))
        cleaned_file_list.append(string_line)
    return cleaned_file_list


def get_graph_labels(file_list):
    i = 0
    label_dictionary = {}
    while file_list[i][0] != "*Arcs":
        label_dictionary[file_list[i][0]] = file_list[i][1]
        i += 1
    return label_dictionary


def get_graph_arcs(file_list):
    i = 0
    arcs_dictionary = {}
    while file_list[i][0] != "*Arcs":
        arcs_dictionary[file_list[i][0]] = file_list[i][1]
        i += 1
    return arcs_dictionary

def get_graph_edges(file_list):
    return [(int(i), int(j)) for i,j in file_list]


def create_adjacency_matrix(edges, vertices):
    adjacency_matrix = []
    for _ in range(0, vertices):
        adjacency_matrix.append([0] * vertices)
    for edge in edges:
        v1, v2 = edge
        adjacency_matrix[v1 - 1][v2 - 1] = 1
        adjacency_matrix[v2 - 1][v1 - 1] = 1
    return adjacency_matrix


def create_incidence_matrix(edges, vertices):
    incidence_matrix = []
    edges.sort()
    for _ in range(0, vertices):
        incidence_matrix.append([0] * len(edges))
    for index, (v1, v2) in enumerate(edges):
        incidence_matrix[v1 - 1][index] = 1
        incidence_matrix[v2 - 1][index] = 1
    return incidence_matrix


def create_neighboorhood_matrix(edges):
    neighboorhood_matrix = {}
    for i, j in edges:
        if i not in neighboorhood_matrix:
            neighboorhood_matrix[i] = [j]
        else:
            neighboorhood_matrix[i].append(j)
    for i in neighboorhood_matrix.values():
        i.sort()
    return neighboorhood_matrix


def get_graph_information(file_path):
    file_list = read_and_cleane_file(file_path)
    matrix_dictionary = {}
    vertices, edges, labels, arcs = int(file_list[0][1]), None, None, None
    file_list.pop(0)
    if file_list[0] != '*Arcs':
        labels = get_graph_labels(file_list)
        index = get_index_of_file_part_in_list(file_list, '*Arcs')
        del file_list[0:index]
    if file_list[1] != '*Edges':
        arcs = get_graph_arcs(file_list)
        index = get_index_of_file_part_in_list(file_list, '*Edges')
        del file_list[0:index]
    file_list.pop(0)
    edges = get_graph_edges(file_list)
    matrix_dictionary['Adjacency Matrix'] = create_adjacency_matrix(edges, vertices)
    matrix_dictionary['Graph Neighborhood Matrix'] = create_neighboorhood_matrix(edges)
    matrix_dictionary['Incidence Matrix'] = create_incidence_matrix(edges, vertices)
    del file_list
    return Graph(vertices, edges, labels, arcs, matrix_dictionary)


def incidence_to_edges(incidence_matrix):
    edges = []
    for col in range(len(incidence_matrix[0])):
        edge = []
        for row in range(len(incidence_matrix)):
            if incidence_matrix[row][col] == 1:
                edge.append(row + 1)
        edges.append(tuple(edge))
    edges.sort()
    return edges


def adjacency_to_edges(adjacency_matrix):
    edges = []
    for i in range(len(adjacency_matrix)):
        for j in range(i + 1, len(adjacency_matrix)):
            if adjacency_matrix[i][j] == 1:
                edges.append((i + 1, j + 1))
    edges.sort()
    return edges


def neighborhood_to_edges(neighborhood_matrix):
    edges = []
    for key, value in neighborhood_matrix.items():
        for item in value:
            edges.append((key, item))
    edges.sort()
    return edges

def last_vertice(edges):
    biggest_vertice = 0
    for edge in edges:
        biggest_vertice = max(biggest_vertice, max(edge))
    return biggest_vertice