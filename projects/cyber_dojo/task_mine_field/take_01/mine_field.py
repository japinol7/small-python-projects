from copy import deepcopy
from enum import Enum


class Cell(str, Enum):
    EMPTY = '.'
    MINE = '*'


class MineField:
    def __init__(self, board):
        self.n_rows = int(board[0])
        self.n_columns = int(board[2])
        self.board = [list(row) for row in board.splitlines()[1:]]

    def _count_neighbours(self, n_row, n_column):
        count = 0
        for x in range(max(n_column - 1, 0), min(n_column + 2, self.n_columns)):
            for y in range(max(n_row - 1, 0), min(n_row + 2, self.n_rows)):
                if all((x != n_column or y != n_row,
                        self.board[y][x] == Cell.MINE.value)):
                    count += 1
        return count

    def resolve(self):
        res = deepcopy(self.board)
        for n_row in range(self.n_rows):
            for n_column in range(self.n_columns):
                if self.board[n_row][n_column] == Cell.MINE.value:
                    res[n_row][n_column] = Cell.MINE.value
                    continue
                res[n_row][n_column] = str(self._count_neighbours(n_row, n_column))
        return '\n'.join((''.join(column) for column in res))
