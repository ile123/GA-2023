def function_3(matrix):
    for i in range(len(matrix)):
        counter = 0
        for j in range(len(matrix)):
            if matrix[j][i] not in (0, 1):
                return False
            if matrix[j][i] == 1:
                counter += 1
                if counter > 2:
                    return False
    return True
