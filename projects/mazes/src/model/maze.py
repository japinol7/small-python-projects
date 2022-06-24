"""Module maze."""
__author__ = 'Joan A. Pinol  (japinol)'

import os
import random

from config.config import (
    MAZE_ROWS_DEFAULT,
    MAZE_COLUMNS_DEFAULT,
    MAZE_SPARSENESS_ROWS_COLS_BASE,
    MAZE_SPARSENESS_DEFAULT,
    CELL_SEPARATOR,
    FILE_INPUT_PATH,
    FILE_OUTPUT_PATH,
    )
from model.cell import Cell
from utils.utils import Point


class Maze:
    def __init__(self, name):
        self.name = name
        self.rows = None
        self.columns = None
        self.start = None
        self.goal = None
        self.sparseness = None
        self.grid = None

        self.file_name = self.name + '.txt'

    def create(self, rows=MAZE_ROWS_DEFAULT, columns=MAZE_COLUMNS_DEFAULT,
               start=None, goal=None, sparseness=MAZE_SPARSENESS_DEFAULT, ):
        self.rows = rows
        self.columns = columns
        self.start = Point(start[0], start[1]) if start else Point(random.randint(0, self.columns - 1), 0)
        self.goal = Point(goal[0], goal[1]) if goal else Point(random.randint(0, self.columns - 1), self.rows - 1)
        if MAZE_SPARSENESS_ROWS_COLS_BASE < rows * columns:
            ratio = MAZE_SPARSENESS_ROWS_COLS_BASE / (rows * columns)
        else:
            ratio = 1
        self.sparseness = sparseness * ratio
        self.grid = None

        self._create()

    def _create(self):
        self._clean_grid()
        for i in range(self.rows):
            self._random_fill()
            self.grid[self.start.y][self.start.x] = Cell.START.value
            self.grid[self.goal.y][self.goal.x] = Cell.GOAL.value

    def _clean_grid(self):
        self.grid = [[Cell.EMPTY.value for _ in range(self.columns)]
                     for r in range(self.rows)]

    def _random_fill(self):
        for i in range(self.rows):
            for j in range(self.columns):
                if random.uniform(0, 1.0) < self.sparseness:
                    self.grid[i][j] = Cell.WALL.value

    def load(self):
        file_path_name = os.path.join(FILE_INPUT_PATH, self.name + '.txt')
        with open(file_path_name, 'r', encoding='utf8') as fin:
            rows = fin.readlines()

        self.grid = []
        for row in rows:
            self.grid.append(row.strip().split(CELL_SEPARATOR))

        self.rows = len(self.grid)
        self.columns = len(self.grid[0])
        self.start = Point(self.grid[0].index(Cell.START.value), 0)
        self.goal = Point(self.grid[-1].index(Cell.GOAL.value), len(self.grid) - 1)

    def save(self, save_as_input=False):
        file_path = FILE_INPUT_PATH if save_as_input else FILE_OUTPUT_PATH
        file_path_name = os.path.join(file_path, self.name + '.txt')
        with open(file_path_name, 'w', encoding='utf8') as fout:
            fout.write(str(self))

    def save_with_no_solution(self, save_as_input=False):
        file_path = FILE_INPUT_PATH if save_as_input else FILE_OUTPUT_PATH
        file_path_name = os.path.join(file_path, self.name + '.txt')
        with open(file_path_name, 'w', encoding='utf8') as fout:
            fout.write("No solutions found. Original maze:\n")
            fout.write(str(self))

    def calc_destination_locations(self, location):
        """Calculate viable neighbour destination locations."""
        point = location
        locations = []
        if point.y + 1 < self.rows and self.grid[point.y + 1][point.x] != Cell.WALL.value:
            locations += [Point(point.x, point.y + 1)]
        if point.y - 1 >= 0 and self.grid[point.y - 1][point.x] != Cell.WALL.value:
            locations += [Point(point.x, point.y - 1)]
        if point.x + 1 < self.columns and self.grid[point.y][point.x + 1] != Cell.WALL.value:
            locations += [Point(point.x + 1, point.y)]
        if point.x - 1 >= 0 and self.grid[point.y][point.x - 1] != Cell.WALL.value:
            locations += [Point(point.x - 1, point.y)]
        return locations

    def check_goal(self, location):
        return location == self.goal

    def mark_path(self, path):
        for location in path:
            self.grid[location.y][location.x] = Cell.PATH.value
        self.grid[self.start.y][self.start.x] = Cell.START.value
        self.grid[self.goal.y][self.goal.x] = Cell.GOAL.value

    def clean_path(self, path):
        for location in path:
            self.grid[location.y][location.x] = Cell.EMPTY.value
        self.grid[self.start.y][self.start.x] = Cell.START.value
        self.grid[self.goal.y][self.goal.x] = Cell.GOAL.value

    def __str__(self):
        res = ''
        for row in self.grid:
            res += CELL_SEPARATOR.join([cell for cell in row]) + '\n'
        return res

    def __repr__(self):
        return self.__str__()
