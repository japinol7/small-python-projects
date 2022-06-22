"""Module node."""
__author__ = 'Joan A. Pinol  (japinol)'


class Node:
    last_node = None

    def __init__(self, state, parent, cost=0, heuristic=0):
        self.state = state
        self.parent = parent
        self.cost = cost
        self.heuristic = heuristic

        if self.parent:
            self.__class__.last_node = self

    def __lt__(self, other):
        return (self.cost + self.heuristic) < (other.cost + other.heuristic)

    def __str__(self):
        return str(self.state)

    def __repr__(self):
        return self.__str__()
