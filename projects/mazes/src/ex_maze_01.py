"""Creates and solves a maze of NxN cells with a start and a goal."""

__author__ = 'Joan A. Pinol  (japinol)'

from config.config import log
from utils.time_it import time_it
from utils.utils import calc_path_from_location_node
from config.config import LOG_START_APP_MSG, LOG_END_APP_MSG
from model.maze import Maze
from solver import dfs


def create_maze(name, load_maze=False):
    """Creates and returns a maze either by loading an existing one or generating a new one randomly."""
    log.info(f"Create maze: {name}")
    maze = Maze(name)
    if load_maze:
        maze.load()
    else:
        maze.create(rows=12, columns=12)
        maze.save(save_as_input=True)
    log.info(f"Maze Start location: {maze.start}. Maze Goal location: {maze.goal}")
    return maze


def solve_maze(maze, save_maze=False):
    """Solves a given maze as a side effect.
    It returns the solution node if it finds one. Otherwise, None.
    """
    solution_node = dfs(maze.start, maze.check_goal, maze.calc_destination_locations)
    if not solution_node:
        log.warning("No solutions found.")
        return None
    log.info(f"Solution found: {solution_node}")
    path = calc_path_from_location_node(solution_node)
    maze.mark_path(path)

    if save_maze:
        maze.save()
    return solution_node


def main():
    log.info(LOG_START_APP_MSG)
    maze_name = 'maze_01'
    maze = time_it(create_maze, name=maze_name, load_maze=True)
    print(maze)

    solution_node = time_it(solve_maze, maze=maze, save_maze=True)
    if solution_node:
        print(maze)
    log.info(LOG_END_APP_MSG)


if __name__ == "__main__":
    main()
