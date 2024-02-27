from batistic_ilario_zad1 import function_1
from batistic_ilario_zad2 import function_2
from batistic_ilario_zad3 import function_3
from batistic_ilario_zad4 import function_4
from batistic_ilario_zad5 import function_5

def main():
    #print(f"Intersecting numbers between two arrays are: {function_1([1, 2, 3, 4, 5], [5, 1, 3, 8, 9])}")
    #print(f'Number of neighbour vowels are: {function_3("geeksforgeeks")}')
    a = int(input("Enter first number of the first range: "))
    b = int(input("Enter second number of the first range: "))
    c = int(input("Enter first number of the second range: "))
    d = int(input("Enter second number of the second range: "))
    print(f"Numbers that are in the section are: {function_2((a, b), (c, d))}")
    #function_4()
    #print(f"Biggest number in the list is: {function_5([72, 18, 3, 'a', True, (2,3)])}")

if __name__ == "__main__":
    main()