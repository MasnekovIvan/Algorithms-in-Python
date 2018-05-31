# faster pow


def pow(a: float, n: int):
    if n == 0:
        return 1
    elif n % 2 == 1:  # for composite numbers
        return pow(a, n - 1) * a
    else:  # for prime numbers
        return pow(a ** 2, n // 2)


print(pow(2, 100))