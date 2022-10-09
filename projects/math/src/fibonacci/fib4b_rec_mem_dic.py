"""Calculates the n element of the Fibonacci sequence.
The Fibonacci sequence:  0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
Where F(0) = 0, F(1) = 1 and F(n) = F(n - 1) + F(n - 2) for n > 1.
So, each term greater than 1 is generated by adding the previous two terms.
For example, the 6th element of the sequence is 8.
It uses a dynamic programming memoized solution using a dictionary and a decorator.
Applying functools.wraps to the wrapper closure returned by the decorator
carries over the docstring and other metadata of the input function.
Benchmarks function fib with the user created function time_it.
"""
__author__ = 'Joan A. Pinol  (japinol)'

from functools import wraps

from fibonacci.time_it import time_it


def cache_memo(func):
    """Caches a given function. It is intended to be used as a decorator."""
    cache = {}

    @wraps(func)
    def wrapper(*args):
        if args not in cache:
            cache[args] = func(*args)
        return cache[args]
    return wrapper


@cache_memo
def fib(n):
    if n < 0:
        return None
    if n <= 2:
        return 1
    return fib(n - 1) + fib(n - 2)


if __name__ == '__main__':
    n = 35
    res = time_it(fib, n)
    print(f'fib({n}): {res}')