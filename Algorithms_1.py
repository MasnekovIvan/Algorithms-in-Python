# brute force, is number simple


def is_simple_number(x):
    """ Определяет, является ли число простым.
        х - целове положительное число.
        Если простое, то возвращает True,
        а иначе - False
    """
    divisor = 2
    while divisor < x:
        if x % divisor == 0:
            return False
        divisor += 1
    return True


print(is_simple_number(69))
