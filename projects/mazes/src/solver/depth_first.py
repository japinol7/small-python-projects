"""Module depth_first."""
__author__ = 'Joan A. Pinol  (japinol)'

from container import Stack
from model.node import Node


def calc_dfs(start_location, check_goal, calc_destination_locations):
    """Implements depth-first algorithm for traversing a graph or tree data structure."""
    next_node = Stack()
    next_node.push(Node(start_location, None))
    explored = {start_location}

    while not next_node.is_empty:
        current_node = next_node.pop()
        current_state = current_node.state
        if check_goal(current_state):
            return current_node
        for location in calc_destination_locations(current_state):
            if location in explored:
                continue
            explored.add(location)
            next_node.push(Node(location, current_node))
    return None
