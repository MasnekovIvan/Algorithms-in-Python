""" Сдвиг элементов массива влево и вправо
    через использование временной переменной
"""


def shift_array_left(A: list, N: int, x: int):
    tmp = A[0]
    for k in range(N-1):
        A[k] = A[k+1]
    A[N-1] = tmp


def shift_array_right(A: list, N: int, x: int):
    tmp = A[N-1]
    for k in range(N-2, -1, -1):
        A[k+1] = A[k]
    A[0] = tmp


def test_shift_left():
    A1 = [1, 2, 3, 4, 5]
    print(A1)
    shift_array_left(A1, 5, 1)
    print(A1)
    if A1 == [2, 3, 4, 5, 1]:
        print("#test1 - ok")
    else:
        print("#test2 - fail")


def test_shift_right():
    A2 = [1, 2, 3, 4, 5]
    print(A2)
    shift_array_right(A2, 5, 1)
    print(A2)
    if A2 == [5, 1, 2, 3, 4]:
        print("#test2 - ok")
    else:
        print("#test2 - fail")


test_shift_left()
test_shift_right()