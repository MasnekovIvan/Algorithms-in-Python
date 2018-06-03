# O(2^n) and memoization Fibonacci`s sequence
from functools import lru_cache


# @lru_cache(maxsize=1000)  # cache version with import functools
def fibonacci(n):  # O(2^n)
    if type(n) != int:
        raise TypeError("n must be a positive int")
    if n < 1:
        raise TypeError("n must be a positive int")

    if n == 1:
        return 1
    elif n == 2:
        return 2
    elif n > 2:
        return fibonacci(n-1) + fibonacci(n-2)


for n in range(1, 10):
    print(n, ":", fibonacci(n))
# for n in range(1, 51):
#     print(fibonacci(n+1) / fibonacci(n))  # "Golden ration" only works with @lru_cache uncomment

""" memoization version

memo = {}


def fibonacci_memo(n):
    if n in memo:
        return memo[n]
    if n == 1:
        value = 1
    elif n == 2:
        value = 1
    elif n > 2:
        value = fibonacci_memo(n-1) + fibonacci_memo(n-2)

    memo[n] = value
    return value


# for n in range(1, 1001):
#     print(n, ":", fibonacci_memo(n))

"""