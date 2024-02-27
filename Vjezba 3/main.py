from batistic_ilario_zad1 import function_1
from batistic_ilario_zad2 import function_2
from batistic_ilario_zad3 import function_3
from batistic_ilario_zad4 import function_4
from batistic_ilario_zad5 import function_5

def main():
    print(f"Sum of main and secondary diagonal is: {function_1()}")
    print(f"Sum of all rows in a matrix is: {function_2([[1, 2, 3], [4, 5, 6], [7, 8, 9]])}")
    print(f"Does the matrix have only 1 and 0: {function_3([[1, 0, 1, 0], [0, 1, 0, 1], [1, 0, 1, 0], [0, 1, 0, 1]])}")
    result_1 = function_4("dictionary_file.txt")
    print(f"Dictionary created from file: {result_1}")
    result_2 = function_5({1:[2,3,5], 2:[1, 4], 3:[1,2]})
    print(f"Inverted dictionary: {result_2}")

if __name__ == "__main__":
    main()