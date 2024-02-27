def is_prime(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


def d(n):
    if n % 2 != 0:
        print("Number is not even!")
        return
    for i in range(1, n):
        for j in range(1, n):
            if is_prime(i) and is_prime(j):
                if i + j == n:
                    print(f"Following prime numbers equal to n: {str(i)} {str(j)}")