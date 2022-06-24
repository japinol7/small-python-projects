"""Module priority_queue."""
__author__ = 'Joan A. Pinol  (japinol)'

from heapq import heappush, heappop


class PriorityQueue:
    def __init__(self):
        self._container = []

    @property
    def is_empty(self):
        return not self._container

    def push(self, item):
        heappush(self._container, item)

    def pop(self):
        return heappop(self._container)

    def __str__(self):
        return repr(self._container)

    def __repr__(self):
        return repr(self._container)
