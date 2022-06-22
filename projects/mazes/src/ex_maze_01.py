"""Creates a maze of NxN cells with a start and a goal.
Also, solves a maze.
"""

__author__ = 'Joan A. Pinol  (japinol)'

from config.config import log
from utils.time_it import time_it
from config.config import LOG_START_APP_MSG, LOG_END_APP_MSG
from maze import Maze
# from path_search import dfs, calc_path_from_location_node


def main(load_maze=False):
    log.info(LOG_START_APP_MSG)

    maze = Maze('maze_01')
    if load_maze:
        maze.load()
    else:
        maze.create(rows=12, columns=12)
        maze.save()
    log.info(f"Maze Start location: {maze.start}. Maze Goal location: {maze.goal}")

    log.info(LOG_END_APP_MSG)
    return maze


if __name__ == "__main__":
    maze = time_it(main, load_maze=True)
    print(maze)

    # solution_node = dfs(maze.start, maze.check_goal, maze.calc_destination_locations)
    # if not solution_node:
    #     log.warning("No solutions found.")
    #     exit()
    # log.info(f"Solution found: {solution_node}")
    # path = calc_path_from_location_node(solution_node)
    # maze.mark_path(path)
    # print(maze)
