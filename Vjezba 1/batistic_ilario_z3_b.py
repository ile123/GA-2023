def b(n):
    counter, i = 1, 1
    flag = False
    while True:
        j = 2
        while j < i:
            if i % j == 0:
                flag = False
                break
            flag = True
            j += 1
        if flag:
            counter += 1
        if counter == n:
            break
        i += 1
    return i
