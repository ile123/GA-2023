def is_square(matrix):
    return len(matrix) == len(matrix[0])

def get_matrix_from_file(file_path):
    file = open(file_path, "r").readlines()
    if not file:
        raise Exception("ERROR: File is either or empty or not found!")
    matrix = []
    for line in file:
        string_line = line.replace("\n", "").split(" ")
        number_line = [int(x) for x in string_line]
        matrix.append(number_line)
    return matrix

def calculate_sum_of_main_diagonal(matrix):
    sum, k = 0, 0
    for i in range(len(matrix)):
        for j in range(k + 1, len(matrix[i])):
            sum += matrix[i][j]
        k += 1
    return sum

def calculate_sum_of_secondary_diagonal(matrix):
    sum, k = 0, len(matrix[0]) - 1
    for i in range(len(matrix)):
        for j in range(k - 1, -1, -1):
            sum += matrix[i][j]
        k -= 1
    return sum

def function_1():
    matrix = get_matrix_from_file("matrix_file.txt")
    if not is_square(matrix):
        return (0, 0)
    return (calculate_sum_of_main_diagonal(matrix), calculate_sum_of_secondary_diagonal(matrix))