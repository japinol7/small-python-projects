CELL_FILL = ' '
CELL_WHITE_SPACE = '  '
CELL_X = 'X '
CELL_FILL_PRETTY = f'{CELL_FILL}{CELL_WHITE_SPACE}'
CELL_X_PRETTY = f'{CELL_X}{CELL_WHITE_SPACE}'


def get_filled_diamond_in_square_grid(size):
    if size % 2 == 0:
        print("User Error. You must supply an odd number, "
              f" but you provided: {size} !")
        return

    upper_half_diamond = []
    for i in range(size + 1):
        upper_half_diamond.append(CELL_FILL * (size - i) + CELL_X * i)
    lower_half_diamond = list(reversed(upper_half_diamond[:-1]))

    return upper_half_diamond + lower_half_diamond


def print_filled_diamond_in_square_grid(grid):
    for row in grid:
        print(''.join(row).replace(CELL_FILL, CELL_FILL_PRETTY).replace(CELL_X, CELL_X_PRETTY))


def main():
    grid = get_filled_diamond_in_square_grid(11)
    if not grid:
        return
    print_filled_diamond_in_square_grid(grid)


if __name__ == '__main__':
    main()
