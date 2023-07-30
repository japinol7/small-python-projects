from collections import deque


class Stack:
    def __init__(self, name=''):
        self._container = deque()
        self.name = name

    @property
    def is_empty(self):
        return not self._container

    def push(self, item):
        self._container.append(item)

    def pop(self):
        return self._container.pop()

    def __str__(self):
        return repr(self._container)

    def __repr__(self):
        return repr(self._container)
