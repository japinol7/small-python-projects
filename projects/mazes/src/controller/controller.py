"""Module controller."""
__author__ = 'Joan A. Pinol  (japinol)'

from config.config import log
from utils.utils import calc_path_from_location_node
from model.maze import Maze


class MazeController:

    @staticmethod
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

    @staticmethod
    def solve_maze(maze, calc_solver, save_maze=False):
        """Solves a given maze as a side effect.
        It returns the solution node if it finds one. Otherwise, None.
        """
        solution_node = calc_solver(maze.start, maze.check_goal, maze.calc_destination_locations)
        if not solution_node:
            log.warning("No solutions found.")
            return None
        log.info(f"Solution found: {solution_node}")
        path = calc_path_from_location_node(solution_node)
        maze.mark_path(path)

        if save_maze:
            maze.save()
        return solution_node
