CELL_FILL = '.'
CELL_X = 'X'
CELL_WHITE_SPACE = '  '
CELL_FILL_PRETTY = f'{CELL_FILL}{CELL_WHITE_SPACE}'
CELL_X_PRETTY = f'{CELL_X}{CELL_WHITE_SPACE}'


def get_diamond_in_square_grid(size):
    if size % 2 == 0:
        print("User Error. You must supply an odd number, "
              f" but you provided: {size} !")
        return

    grid = [[CELL_FILL for _ in range(size)] for __ in range(size)]
    half_size = size // 2

    column_pos_1 = half_size
    column_pos_2 = half_size + 1
    for i, row in enumerate(grid):
        row[column_pos_1] = CELL_X
        column_pos_1 += 1 if i < half_size else -1
        column_pos_2 -= 1 if i < half_size + 1 else -1
        row[column_pos_2] = CELL_X
    return grid


def print_diamond_in_square_grid(grid):
    for row in grid:
        print(''.join(row).replace(CELL_FILL, CELL_FILL_PRETTY).replace(CELL_X, CELL_X_PRETTY))


def main():
    grid = get_diamond_in_square_grid(15)
    if not grid:
        return
    print_diamond_in_square_grid(grid)


if __name__ == '__main__':
    main()
