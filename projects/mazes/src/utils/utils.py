"""Module utils."""
__author__ = 'Joan A. Pinol  (japinol)'

from typing import NamedTuple


class Point(NamedTuple):
    x: int
    y: int


def calc_path_from_location_node(node):
    path = [node.state]
    while node.parent is not None:
        node = node.parent
        path += [node.state]
    return path


def linear_search(iterable, key):
    for item in iterable:
        if item == key:
            return True
    return False


def binary_search(sequence, key):
    low = 0
    high = len(sequence) - 1
    while low <= high:
        mid = (low + high) // 2
        if sequence[mid] < key:
            low = mid + 1
        elif sequence[mid] > key:
            high = mid - 1
        else:
            return True
    return False
