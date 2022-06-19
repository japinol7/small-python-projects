"""Module time_it_dec."""
__author__ = 'Joan A. Pinol  (japinol)'

from functools import wraps
import time

from config.config import log


def time_it(func):
    """Benchmarks a given function. It is intended to be used as a decorator."""
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        res = func(*args, **kwargs)
        log.info(f'{func.__name__} t: {time.time() - start:.8f} s')
        return res
    return wrapper
