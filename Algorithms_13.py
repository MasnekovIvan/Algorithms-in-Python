# merge sort


def merge(A: list, B: list):  # merge A[] + B[] into C[]
    """ Сортировка методом слияния """
    C = [0] * (len(A) + len(B))
    i = k = n = 0
    while i < len(A) and k < len(B):
        if A[i] <= B[k]:
            C[n] = A[i]
            i += 1
            n += 1
        else:
            C[n] = B[k]
            k += 1
            n += 1
    while i < len(A):
        C[n] = A[i]
        i += 1
        n += 1

    while k < len(B):
        C[n] = B[k]
        k += 1
        n += 1
    return C


def merge_sort(A):  # sort
    if len(A) <= 1:
        return
    middle = len(A)//2
    L = [A[i] for i in range(0, middle)]
    R = [A[i] for i in range(middle, len(A))]
    merge_sort(L)
    merge_sort(R)
    C = merge(L, R)
    for i in range(len(A)):
        A[i] = C[i]


def test_merge():
    print("testcase #1: ", end="")
    A = [0, 1, 2, 3, 4]
    B = [5, 6, 7, 8, 9]
    C_sorted = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    C = merge(A, B)
    print("Ok" if C == C_sorted else "Fail")  # ternary operator
    print(C)

    print("testcase #1: ", end="")
    A = [0, 1, 2]
    B = [3, 4, 5, 6, 7, 8, 9]
    C_sorted = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    C = merge(A, B)
    print("Ok" if C == C_sorted else "Fail")  # ternary operator
    print(C)

    print("testcase #1: ", end="")
    A = [5, 1, 4, 3, 2, 8, 6]
    merge_sort(A)
    B = [6, 9, 0, 7, 8, 0, 3]
    merge_sort(B)
    C_sorted = [0, 0, 1, 2, 3, 3, 4, 5, 6, 6, 7, 8, 8, 9]
    C = merge(A, B)
    print("Ok" if C == C_sorted else "Fail")  # ternary operator
    print(C)

test_merge()