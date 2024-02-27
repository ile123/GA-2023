def function_4(file_path):
    file = open(file_path, "r").readlines()
    if not file:
        raise Exception("ERROR: File is either or empty or not found!")
    dictionary = {}
    for line in file:
        string_line = line.replace("\n", "").split(" ")
        number_line = [int(x) for x in string_line]
        dictionary[number_line[0]] = number_line[1]
    return dictionary