"""Creates a maze of NxN cells with a start and a goal."""

__author__ = 'Joan A. Pinol  (japinol)'

from time_it.time_it import time_it
from maze import Maze


def main():
    maze = Maze('maze_01')
    maze.create(rows=12, columns=12)
    maze.save()
    return maze


if __name__ == "__main__":
    res = time_it(main)
    print(res)
