# Tony Hoare`s sort (Quicksort)


def hoare_sort(A):
    """ Сортировка Тони Хоара (Quicksort) """
    if len(A) <= 1:
        return
    barrier = A[0]
    L = []
    M = []
    R = []
    for x in A:
        if x < barrier:
            L.append(x)
        elif x == barrier:
            M.append(x)
        else:
            R.append(x)
    hoare_sort(L)
    hoare_sort(R)
    k = 0
    for x in L + M + R:
        A[k] = x
        k += 1


def check_sorted(A, ascending=True):
    """ Проверка отсортированности за O(len(A)) """
    flag = True
    s = 2 * int(ascending) - 1
    N = len(A)
    for i in range(0, N-1):
        if s * A[i] > s * A[i+1]:
            flag = False
            break
    return flag


def test_hoare():  # test sorting and check is sorting True
    print("testcase #1: ", end="")
    A = [5, 1, 4, 3, 2, 8, 6]
    A_sorted = [1, 2, 3, 4, 5, 6, 8]
    hoare_sort(A)
    print("Ok" if A == A_sorted else "Fail")  # ternary operator
    print("End result of sorting is:", check_sorted(A))

    print("testcase #2: ", end="")
    A = [1, 0, 0, 3, 5, 6, 7, 1, 1]
    A_sorted = [0, 0, 1, 1, 1, 3, 5, 6, 7]
    hoare_sort(A)
    print("Ok" if A == A_sorted else "Fail")  # ternary operator
    print("End result of sorting is:", check_sorted(A))

    print("testcase #3: ", end="")
    A = [0, 1, 0, 1, 1, 0, 1, 0]
    A_sorted = [0, 0, 0, 0, 1, 1, 1, 1]
    hoare_sort(A)
    print("Ok" if A == A_sorted else "Fail")  # ternary operator
    print("End result of sorting is:", check_sorted(A))


test_hoare()