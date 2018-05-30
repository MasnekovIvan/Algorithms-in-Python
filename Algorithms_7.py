# eratosthenes sieve

def eratosthenes_sieve(A: list, N: int):
    A = [True] * N
    A[0] = A[1] = False
    for k in range(2, N):
        if A[k]:
            for m in range(2*k, N, k):
                A[m] = False
    for k in range(N):
        print(k, '-', "prime number" if A[k] else "composite number") # ternary operator

def test_eratosthenes_sieve():
    A1 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
    eratosthenes_sieve(A1, 20)

test_eratosthenes_sieve()