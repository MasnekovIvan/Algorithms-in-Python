# binary search in array
""" Требование: массив отсортирован """


def left_bound(A, key):
    left = -1
    right = len(A)
    while right - left > 1:
        middle = (left + right)//2
        if A[middle] < key:
            left = middle
        else:
            right = middle
    return left


def right_bound(A, key):
    left = -1
    right = len(A)
    while right - left > 1:
        middle = (left + right)//2
        if A[middle] <= key:
            left = middle
        else:
            right = middle
    return right


def test_sort():
    A = [1, 1, 2, 3, 4, 4, 4, 4, 5, 6, 6, 7]
    key = 4
    print(A)
    print("Left bound of", key, "is:", left_bound(A, key))
    print("Right bound of", key, "is:", right_bound(A, key))


test_sort()