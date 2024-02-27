def is_prime(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


def c(n):
    array = []
    for i in range(1, n):
        if is_prime(i) and is_prime(i + 2):
            array.append((i, i + 2))
    return array