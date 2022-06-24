"""Module queue."""
__author__ = 'Joan A. Pinol  (japinol)'


from collections import deque


class Queue:
    def __init__(self):
        self._container = deque()

    @property
    def is_empty(self):
        return not self._container

    def push(self, item):
        self._container.append(item)

    def pop(self):
        return self._container.popleft()

    def __str__(self):
        return repr(self._container)

    def __repr__(self):
        return repr(self._container)
