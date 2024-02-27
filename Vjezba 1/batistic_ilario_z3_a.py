import math

def a(n, m):
    j = math.ceil(n) if n % 1 > 0.5 else math.floor(n)
    k = math.ceil(m) if n % 1 > 0.5 else math.floor(m)
    counter = 0
    flag = True
    if n > m:
        for a in range(k, j):
            for b in range(2, k):
                if a % b == 0:
                    flag = False
                    break
            if flag:
                counter += 1
            flag = True
    else:
        for a in range(j, k):
            for b in range(2, j):
                if a % b == 0:
                    flag = False
                    break
            if flag:
                counter += 1
            flag = True
    return counter

