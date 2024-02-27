""" array = [i]
        counter, temp = 1, i
        while counter <= i:
            if i // 2 >= counter:
                temp += 1
                if temp > 9:
                    temp = 0
                array.append(temp)
            else:
                temp -= 1
                if temp < 0:
                    temp = 9
                array.append(temp)
            counter += 1
        print(array) """

#dovrsi kasnije
def function_2(n):
    if n >= 20:
        print("\n"
              "--------------------------------------------------------------------------------------------"
              "\nNumber has to be smaller then 20!\n"
              "--------------------------------------------------------------------------------------------"
              "\n")
        return
    step_increase = 0
    for i in range(1, n + 1):
        array = [i]
        counter, temp = 1, i
        while counter < i + step_increase:
            if step_increase >= counter:
                temp += 1
                if temp > 9:
                    temp = 0
                array.append(temp)
            else:
                temp -= 1
                if temp < 0:
                    temp = 9
                array.append(temp)
            counter += 1
        print(*array)
        step_increase += 1