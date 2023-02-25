import os
import itertools


def get_first_lines_from_file(filename, qty):
    with open(filename, "r") as file:
        return itertools.islice(file.read().splitlines(), qty)


def main():
    filename = os.path.join('..', 'res', 'data', 'names1.txt')
    res = list(get_first_lines_from_file(filename, 2))
    print(res)


if __name__ == '__main__':
    main()
