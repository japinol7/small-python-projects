class GameOfLifeException(Exception):
    pass


class GameOfLife:

    def __init__(self, rows_n, cols_n, grid_str):
        self.rows_n = rows_n
        self.cols_n = cols_n

        self._validate_input(grid_str)

        self.grid = GameOfLife._str_to_grid(grid_str)

    def calc_next_generation(self):
        return GameOfLife._grid_to_str(self._calc_next_generation_rules())

    def _calc_next_generation_rules(self):
        new_grid = [['.'] * self.cols_n for _ in range(self.rows_n)]
        for row in range(self.rows_n):
            for col in range(self.cols_n):
                is_alive = self.grid[row][col] == '*'
                neighbours_n = self.count_neighbours(row, col)
                if is_alive and neighbours_n < 2:
                    new_grid[row][col] = '.'
                elif is_alive and neighbours_n > 3:
                    new_grid[row][col] = '.'
                elif is_alive and neighbours_n in {2, 3}:
                    new_grid[row][col] = '*'
                elif not is_alive and neighbours_n == 3:
                    new_grid[row][col] = '*'
        return new_grid

    def count_neighbours(self, row, col):
        neighbours_n = 0

        if row - 1 >= 0 and self.grid[row - 1][col] == '*':
            neighbours_n += 1
        if row + 1 < self.rows_n and self.grid[row + 1][col] == '*':
            neighbours_n += 1

        if col - 1 >= 0 and self.grid[row][col - 1] == '*':
            neighbours_n += 1
        if col + 1 < self.cols_n and self.grid[row][col + 1] == '*':
            neighbours_n += 1

        if row - 1 >= 0 and col - 1 >= 0 and self.grid[row - 1][col - 1] == '*':
            neighbours_n += 1
        if row - 1 >= 0 and col + 1 < self.cols_n and self.grid[row - 1][col + 1] == '*':
            neighbours_n += 1
        if row + 1 < self.rows_n and col + 1 < self.cols_n and self.grid[row + 1][col + 1] == '*':
            neighbours_n += 1
        if row + 1 < self.rows_n and col - 1 >= 0 and self.grid[row + 1][col - 1] == '*':
            neighbours_n += 1

        return neighbours_n

    def _validate_input(self, grid_str):
        if not self.rows_n or not self.cols_n or not grid_str:
            raise GameOfLifeException("User Error: Invalid input values.")

    @staticmethod
    def _str_to_grid(grid_str):
        return [list(row) for row in grid_str.split('\n')]

    @staticmethod
    def _grid_to_str(grid):
        for row in grid[:-1]:
            row.append('\n')

        grid_flat = sum(grid, [])
        return ''.join(grid_flat)
