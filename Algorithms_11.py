# generate number combinations


def gen_bin(M, prefix=""):  # binary generation
    if M == 0:
        print(prefix)
        return
    for digit in "0", "1":
        gen_bin(M-1, prefix+digit)


def generate_number(N: int, M: int, prefix=None):  # N-count generation
    """ Генерирует все числа (с лидирующими незначащими нулями
        в N-риноый системе счисления (N <= 10)
        длины М
    """
    prefix = prefix or []
    if M == 0:
        print(prefix)
        return
    for digit in range(N):
        prefix.append(digit)
        generate_number(N, M-1, prefix)
        prefix.pop()


# gen_bin(5)
# generate_number(3, 3)
