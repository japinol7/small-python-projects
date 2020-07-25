""" Calculates pi using the Leibniz formula.
    Benchmarks function fib with the user created function time_it.
"""
__author__ = 'Joan A. Pinol  (japinol)'


from time_it.time_it import time_it


def calc_pi(n_terms, n_decimals=None):
    numerator = 4.0
    denominator = 1.0
    operation = 1.0
    pi = 0.0
    for _ in range(n_terms):
        pi += operation * (numerator / denominator)
        denominator += 2.0
        operation *= -1.0
    if n_decimals:
        pi = round(pi, n_decimals)
    return pi


if __name__ == "__main__":
    res = time_it(calc_pi, 5000000, 6)
    print(f'pi: {res}')
