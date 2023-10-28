# TODO: WIP. This kata is in development.

import copy
from enum import Enum
import random

DEFAULT_N_ROWS = 8
DEFAULT_N_COLS = 8
DEFAULT_LIVES = 5
DEFAULT_MINE_CELL_PGE = 0.5

CELL_ADDITIONAL_SPACE = ' '


class Cell(str, Enum):
    NOT_KNOWN: str = '.' + CELL_ADDITIONAL_SPACE
    MINE: str = '*' + CELL_ADDITIONAL_SPACE
    PLAYER: str = 'O' + CELL_ADDITIONAL_SPACE
    VISITED: str = 'o' + CELL_ADDITIONAL_SPACE


class Movement(str, Enum):
    UP: str = 'up'
    DOWN: str = 'down'
    LEFT: str = 'left'
    RIGHT: str = 'right'


class MineSweeper:
    def __init__(self, rows_n=DEFAULT_N_ROWS, cols_n=DEFAULT_N_COLS,
                 mine_cell_pge=DEFAULT_MINE_CELL_PGE, lives=DEFAULT_LIVES):
        self.rows_n = rows_n
        self.cols_n = cols_n
        self.lives = lives
        self.turn = 1
        self.mine_cell_pge = mine_cell_pge
        self.mines_n = 0
        self.board = [[Cell.NOT_KNOWN] * cols_n for _ in range(rows_n)]

    def board_str(self):
        board = copy.deepcopy(self.board)
        for row in board[:-1]:
            row.append('\n')

        grid_flat = sum(board, [])
        return ''.join(grid_flat)

    def add_mines(self):
        for row in range(self.rows_n):
            for col in range(self.cols_n):
                if random.random() + self.mine_cell_pge >= 1:
                    self.board[row][col] = Cell.MINE
                    self.mines_n += 1
