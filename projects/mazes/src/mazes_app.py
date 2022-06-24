"""Creates and solves mazes of NxN cells with a start and a goal."""

__author__ = 'Joan A. Pinol  (japinol)'

from argparse import ArgumentParser
import traceback

from utils.time_it import time_it
from config.config import (
    LOG_START_APP_MSG,
    LOG_END_APP_MSG,
    LOG_INPUT_ERROR_MSG,
    MAZE_ROWS_COLS_MAX,
    MAZE_ROWS_COLS_MIN,
    MAZE_ROWS_DEFAULT,
    MAZE_COLUMNS_DEFAULT,
    )
from config.config import log
from solver import calc_dfs
from controller.controller import MazeController


def mazes(maze_name, load_maze, rows, columns, print_maze):
    log.info(LOG_START_APP_MSG)
    controller = MazeController()

    if (rows < MAZE_ROWS_COLS_MIN or rows > MAZE_ROWS_COLS_MAX
            or columns < MAZE_ROWS_COLS_MIN or columns > MAZE_ROWS_COLS_MAX):
        log.info(LOG_INPUT_ERROR_MSG)
        return

    maze = time_it(controller.create_maze, name=maze_name, load_maze=load_maze,
                   rows=rows, columns=columns)
    print_maze and print(maze)

    solution_node = time_it(controller.solve_maze, maze=maze, calc_solver=calc_dfs, save_maze=True)
    if solution_node and print_maze:
        print(maze)
    log.info(LOG_END_APP_MSG)


def main():
    # Parse optional arguments from the command line
    parser = ArgumentParser(description="Maze solver.",
                            prog='mazes_app')
    parser.add_argument('-c', '--create', default=False, action='store_true',
                        help="Create a new maze instead of loading one.")
    parser.add_argument('-p', '--print', default=False, action='store_true',
                        help="Print maze to the console.")
    parser.add_argument('-n', '--name', default=None,
                        help="'the maze's name.'")
    parser.add_argument('-nr', '--rows', default=None,
                        help=f"the number of rows. Must be between {MAZE_ROWS_COLS_MIN} and {MAZE_ROWS_COLS_MAX}.")
    parser.add_argument('-nc', '--columns', default=None,
                        help=f"the number of columns. Must be between {MAZE_ROWS_COLS_MIN} and {MAZE_ROWS_COLS_MAX}.")
    parser.add_argument('-t', '--debugtraces', default=False, action='store_true',
                        help="show debug back traces information when something goes wrong.")

    args = parser.parse_args()
    try:
        mazes(maze_name=args.name or 'maze_01',
              load_maze=not args.create,
              print_maze=args.print,
              rows=args.rows and int(args.rows) or MAZE_ROWS_DEFAULT,
              columns=args.columns and int(args.columns) or MAZE_COLUMNS_DEFAULT,
              )
    except Exception as e:
        if args.debugtraces:
            traceback.print_tb(e.__traceback__)
        log.critical(f'Error: {e}')


if __name__ == "__main__":
    main()
