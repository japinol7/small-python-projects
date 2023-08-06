"""Module priority_queue."""
__author__ = 'Joan A. Pinol  (japinol)'

from heapq import heappush, heappop


class PriorityQueue:
    def __init__(self, name=''):
        self._container = []
        self.name = name

    @property
    def is_empty(self):
        return not self._container

    def push(self, item):
        heappush(self._container, item)

    def pop(self):
        return heappop(self._container)

    def peek(self):
        return self._container[0] if not self.is_empty else None

    def __len__(self):
        return len(self._container)

    def __str__(self):
        return f"PriorityQueue({repr(self._container)})"

    def __repr__(self):
        return f"PriorityQueue({repr(self._container)})"
