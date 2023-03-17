""" Gets the prime factors of a number."""
import math
from time_it.time_it import time_it


def get_prime_factors(num):
    candidate = 2
    while candidate * candidate <= num:
        if num % candidate:
            candidate += 1
        else:
            num //= candidate
            yield candidate

    if num > 1:
        yield num


def main():
    input_num = 3 * 3 * 5 * 2 ** 3 * 17 * 55 * 11 ** 5
    result = list(time_it(get_prime_factors, input_num))
    expected = math.prod(result)
    print(f'Res: {result}')
    print('Test: ' + 'Ok' if input_num == expected else 'Failed!')


if __name__ == '__main__':
    main()
