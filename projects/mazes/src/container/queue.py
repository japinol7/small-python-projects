"""Module queue."""
__author__ = 'Joan A. Pinol  (japinol)'

from collections import deque


class Queue:
    def __init__(self, name=''):
        self._container = deque()
        self.name = name

    @property
    def is_empty(self):
        return not self._container

    def push(self, item):
        self._container.append(item)

    def pop(self):
        return self._container.popleft()

    def peek(self):
        return self._container[0] if not self.is_empty else None

    def __len__(self):
        return len(self._container)

    def __str__(self):
        return f"Queue({repr(list(self._container))})"

    def __repr__(self):
        return f"Queue({repr(list(self._container))})"
