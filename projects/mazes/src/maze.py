from enum import Enum, auto
import os
import random

ROWS_DEFAULT = 15
COLUMNS_DEFAULT = 15
SPARSENESS_DEFAULT = 0.02
CELL_SEPARATOR = '  '

FILE_INPUT_PATH = os.path.join('..', 'input')
FILE_OUTPUT_PATH = os.path.join('..', 'output')


class Cell(str, Enum):
    START = 'S'
    GOAL = 'G'
    EMPTY = '·'
    PATH = '*'
    WALL = 'W'


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"{self.x, self.y}"

    def __repr__(self):
        return self.__str__()


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

    def create(self, rows=ROWS_DEFAULT, columns=COLUMNS_DEFAULT,
               start=None, goal=None, sparseness=SPARSENESS_DEFAULT, ):
        self.rows = rows
        self.columns = columns
        self.start = Point(start[0], start[1]) if start else Point(random.randint(0, self.columns - 1), 0)
        self.goal = Point(goal[0], goal[1]) if goal else Point(random.randint(0, self.columns - 1), self.rows - 1)
        self.sparseness = sparseness
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
        file_path_name = os.path.join(FILE_OUTPUT_PATH, self.name + '.txt')
        with open(file_path_name, 'r', encoding='utf8') as fin:
            rows = fin.readlines()

        self.grid = []
        for row in rows:
            self.grid.append(row.strip().split(CELL_SEPARATOR))

        self.rows = len(self.grid)
        self.columns = len(self.grid[0])
        self.start = Point(self.grid[0].index(Cell.START.value), 0)
        self.goal = Point(self.grid[-1].index(Cell.GOAL.value), len(self.grid))

    def save(self):
        file_path_name = os.path.join(FILE_OUTPUT_PATH, self.name + '.txt')
        with open(file_path_name, 'w', encoding='utf8') as fout:
            fout.write(str(self))

    def destination_locations(self, location):
        """Viable neighbour destination locations."""
        point = location
        locations = []
        if point.y + 1 < self.rows and self.grid[point.y + 1][point.x] != Cell.WALL:
            locations += [Point(point.x, point.y + 1)]
        if point.y - 1 >= 0 and self.grid[point.y - 1][point.x] != Cell.WALL:
            locations += [Point(point.x, point.y - 1)]
        if point.x + 1 < self.columns and self.grid[point.y][point.x + 1] != Cell.WALL:
            locations += [Point(point.x + 1, point.y)]
        if point.x - 1 >= 0 and self.grid[point.y][point.x - 1] != Cell.WALL:
            locations += [Point(point.x - 1, point.y)]
        return locations

    def __str__(self):
        res = ''
        for row in self.grid:
            res += CELL_SEPARATOR.join([cell for cell in row]) + '\n'
        return res

    def __repr__(self):
        return self.__str__()
