"""Creates and solves mazes of NxN cells with a start and a goal."""

__author__ = 'Joan A. Pinol  (japinol)'

from config.config import log
from utils.time_it import time_it
from config.config import LOG_START_APP_MSG, LOG_END_APP_MSG
from solver import calc_dfs
from controller.controller import MazeController


def main():
    log.info(LOG_START_APP_MSG)
    controller = MazeController()

    maze_name = 'maze_01'
    maze = time_it(controller.create_maze, name=maze_name, load_maze=True)
    print(maze)

    solution_node = time_it(controller.solve_maze, maze=maze, calc_solver=calc_dfs, save_maze=True)
    if solution_node:
        print(maze)
    log.info(LOG_END_APP_MSG)


if __name__ == "__main__":
    main()
