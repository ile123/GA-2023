from batistic_ilario_v5_Graph import Graph

def get_index_of_file_part_in_list(list, part_of_file):
    for index, item in enumerate(list):
        if item[0] == part_of_file:
            return index
    return None


def read_and_cleane_file(file_path):
    cleaned_file_list = []
    with open(file_path, "r") as file:
        contents = file.readlines()
        if not file:
            raise Exception("ERROR: File is either or empty or not found!")
        for line in contents:
            string_line = line.replace("\n", "").split(" ")
            string_line = list(filter(lambda i: i != '', string_line))
            cleaned_file_list.append(string_line)
    return cleaned_file_list


def get_labels(vertice_list):
    label_dictionary = {}
    vertice_list.pop(0)
    for item in vertice_list:
        label_dictionary[item[0]] = item[1]
    return label_dictionary


def get_edges(list):
    list.pop(0)
    return [(int(i), int(j)) for i, j in list]

def get_arcs(list):
    list.pop(0)
    if len(list[0]) == 2:
        return [(int(i), int(j)) for i, j in list]
    else:
        return [(int(i), int(j), int(z)) for i, j, z in list]


def create_adjacency_matrix_from_edges(edges, vertices):
    adjacency_matrix = []
    for _ in range(0, vertices):
        adjacency_matrix.append([0] * vertices)
    for item in edges:
        v1 = item[0] if item[0] == 0 else item[0] - 1
        v2 = item[1] if item[1] == 0 else item[1] - 1
        adjacency_matrix[v1][v2] = 1
        adjacency_matrix[v2][v1] = 1
    return adjacency_matrix

def create_adjacency_matrix_from_arcs(arcs, vertices):
    adjacency_matrix = []
    for _ in range(0, vertices):
        adjacency_matrix.append([0] * vertices)
    for item in arcs:
        v1 = item[0] if item[0] == 0 else item[0] - 1
        v2 = item[1] if item[1] == 0 else item[1] - 1
        adjacency_matrix[v1][v2] = 1
        adjacency_matrix[v2][v1] = 1
    return adjacency_matrix


def create_incidence_matrix_from_edges(edges, vertices):
    incidence_matrix = []
    edges.sort()
    for _ in range(0, vertices):
        incidence_matrix.append([0] * len(edges))
    for index, item in enumerate(edges):
        v1 = item[0] if item[0] == 0 else item[0] - 1
        v2 = item[1] if item[1] == 0 else item[1] - 1
        incidence_matrix[v1][index] = 1
        incidence_matrix[v2][index] = 1
    return incidence_matrix


def create_incidence_matrix_from_arcs(arcs, vertices):
    incidence_matrix = []
    arcs.sort()
    for _ in range(0, vertices):
        incidence_matrix.append([0] * len(arcs))
    for index, item in enumerate(arcs):
        v1 = item[0] if item[0] == 0 else item[0] - 1
        v2 = item[1] if item[1] == 0 else item[1] - 1
        incidence_matrix[v1][index] = 1
        incidence_matrix[v2][index] = 1
    return incidence_matrix


def create_neighboorhood_matrix_from_edges(edges):
    neighboorhood_matrix = {}
    for i, j in edges:
        if i not in neighboorhood_matrix:
            neighboorhood_matrix[i] = [j]
        else:
            neighboorhood_matrix[i].append(j)
    for i in neighboorhood_matrix.values():
        i.sort()
    return neighboorhood_matrix


def create_neighboorhood_matrix_from_arcs(arcs):
    neighboorhood_matrix = {}
    if len(arcs[0]) == 2:
        for i, j in arcs:
            if i not in neighboorhood_matrix:
                neighboorhood_matrix[i] = [j]
            else:
                neighboorhood_matrix[i].append(j)
        for i in neighboorhood_matrix.values():
            i.sort()
    else:
        for i, j, _ in arcs:
            if i not in neighboorhood_matrix:
                neighboorhood_matrix[i] = [j]
            else:
                neighboorhood_matrix[i].append(j)
        for i in neighboorhood_matrix.values():
            i.sort()
    return neighboorhood_matrix


def split_list_by_data(file_list):
    new_list = []
    temp_list = [file_list[0]]
    file_list.pop(0)
    for item in file_list:
        if '*' in item[0]:
            new_list.append(temp_list)
            temp_list = []
            temp_list.append(item)
        else:
            temp_list.append(item)
    new_list.append(temp_list)
    return new_list


def get_graph_information(file_path):
    file_list = split_list_by_data(read_and_cleane_file(file_path))
    vertices, edges, labels, arcs = None, None, None, None
    for item in file_list:
        if item[0][0].lower() == '*vertices':
            if len(item[0]) == 2:
                vertices = int(item[0][1])
                labels = get_labels(item)
            else:
                labels = get_labels(item)
                vertices = len(labels)
        elif item[0][0].lower() == '*arcs' and len(item) > 1:
            arcs = get_arcs(item)
        elif item[0][0].lower() == '*edges' and len(item) > 1:
            print(item[0])
            edges = get_edges(item)
    matrix_dictionary = {}
    matrix_dictionary['Adjacency Matrix'] = create_adjacency_matrix_from_edges(edges, vertices) if edges is not None else create_adjacency_matrix_from_arcs(arcs, vertices)
    matrix_dictionary['Graph Neighborhood Matrix'] = create_neighboorhood_matrix_from_edges(edges) if edges is not None else create_neighboorhood_matrix_from_arcs(arcs)
    matrix_dictionary['Incidence Matrix'] = create_incidence_matrix_from_edges(edges, vertices) if edges is not None else create_incidence_matrix_from_arcs(arcs, vertices)
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