"""Module time_it."""
__author__ = 'Joan A. Pinol  (japinol)'

import time


def time_it(func, *args, **kwargs):
    """Benchmarks a given function."""
    start = time.time()
    res = func(*args, **kwargs)
    print(f'{func.__name__} t: {time.time() - start:.{8}f} s')
    return res
