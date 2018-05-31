# generate number permutations


def find(number, A):
    """ Функция ищет х в А и возвращает True, если такой есть
        Если нет, то возвращает False
    """
    flag = False
    for x in A:
        if number == x:
            flag = True
            break
    return flag


def generate_permutations(N: int, M: int = -1, prefix=None):
    """ Генератор перестановок N-чисел в М позициях,
        начиная с перфиксом prefix
    """
    M = N if M == -1 else M  # default
    prefix = prefix or []
    if M == 0:
        print(*prefix)
        return
    for number in range(1, N+1):
        if find(number, prefix):
            continue
        prefix.append(number)
        generate_permutations(N, M-1, prefix)
        prefix.pop()


generate_permutations(5)