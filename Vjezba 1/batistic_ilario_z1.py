def function_1():
    while 1 == 1:
        print("\nPlease provide us three numbers to check if they are Pythagorean Triples:\n")
        triples = tuple(input('Enter numbers here(put space between them)): ').split())
        if len(triples) != 3:
            print("\n--------------------------------------------------------------------------------------------"
                  "\nInvalid amount of numbers!\n"
                  "--------------------------------------------------------------------------------------------\n")
        else:
            number_array = [int(item) for item in triples]
            c = max(number_array)
            number_array.remove(c)
            a, b = number_array[0], number_array[1]
            if a <= 0 or b <= 0 or c <= 0:
                break
            if (a**2 + b**2) == c**2:
                print("\n"
                      "--------------------------------------------------------------------------------------------"
                      "\nThe numbers are Pythagorean Triples\n"
                      "--------------------------------------------------------------------------------------------"
                      "\n")
            else:
                print("\n"
                      "--------------------------------------------------------------------------------------------"
                      "\nThe numbers are not Pythagorean Triples\n"
                      "--------------------------------------------------------------------------------------------"
                      "\n")
