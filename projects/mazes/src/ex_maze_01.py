"""Creates a maze of NxN cells with a start and a goal."""

__author__ = 'Joan A. Pinol  (japinol)'

from config.config import log
from utils.time_it import time_it
from config.config import LOG_START_APP_MSG, LOG_END_APP_MSG
from maze import Maze


def main():
    log.info(LOG_START_APP_MSG)

    maze = Maze('maze_01')
    maze.create(rows=12, columns=12)
    maze.save()

    log.info(LOG_END_APP_MSG)
    return maze


if __name__ == "__main__":
    maze = time_it(main)
    print(maze)
