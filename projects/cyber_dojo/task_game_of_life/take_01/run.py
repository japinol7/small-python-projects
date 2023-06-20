from game_of_life import GameOfLife

GENERATIONS_N = 5

GRID_VALS = (
    5, 8,
    '........\n'
    '...**...\n'
    '.*****..\n'
    '........\n'
    '........',
    )


def main():
    print(f"Start grid\n{GRID_VALS[2]}\n")

    generations_n = GENERATIONS_N
    game_of_life = GameOfLife(*GRID_VALS)
    for n in range(1, generations_n + 1):
        result = game_of_life.calc_next_generation()
        print(f"Generation {n}\n{result}\n")


if __name__ == '__main__':
    main()
