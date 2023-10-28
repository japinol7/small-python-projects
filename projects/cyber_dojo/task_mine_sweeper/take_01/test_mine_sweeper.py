# TODO: WIP. This kata is in development.

from mine_sweeper import MineSweeper, Cell


class TestMineSweeper:
    def test_create_empty_board(self):
        n_rows = 4
        n_cols = 5
        mine_sweeper = MineSweeper(n_rows, n_cols)
        expected = [
            [Cell.NOT_KNOWN, Cell.NOT_KNOWN, Cell.NOT_KNOWN, Cell.NOT_KNOWN, Cell.NOT_KNOWN],
            [Cell.NOT_KNOWN, Cell.NOT_KNOWN, Cell.NOT_KNOWN, Cell.NOT_KNOWN, Cell.NOT_KNOWN],
            [Cell.NOT_KNOWN, Cell.NOT_KNOWN, Cell.NOT_KNOWN, Cell.NOT_KNOWN, Cell.NOT_KNOWN],
            [Cell.NOT_KNOWN, Cell.NOT_KNOWN, Cell.NOT_KNOWN, Cell.NOT_KNOWN, Cell.NOT_KNOWN],
            ]
        assert len(mine_sweeper.board) == n_rows
        assert len(mine_sweeper.board[0]) == n_cols
        assert mine_sweeper.board == expected

    def test_create_board_with_only_one_mine(self):
        mine_sweeper = MineSweeper(rows_n=4, cols_n=5)
        mine_sweeper.board[0][2] = Cell.MINE
        n_mines = sum((1 for row in mine_sweeper.board for cell in row if cell == Cell.MINE))
        assert n_mines == 1

    def test_add_mines_in_board(self, random_num_for_mines):
        mine_sweeper = MineSweeper(rows_n=8, cols_n=8, mine_cell_pge=0.5)
        mine_sweeper.add_mines()
        expected = (". . * * . . . . \n"
                    "* . * . . * . * \n"
                    ". * . . * . * . \n"
                    "* * . . . * . . \n"
                    "* . . * . * . . \n"
                    ". . * . . . . * \n"
                    ". . . * . . * . \n"
                    ". * . . . . . . ")
        assert mine_sweeper.board_str() == expected
        assert mine_sweeper.mines_n == 20
        print(f"\n{mine_sweeper.board_str()}")
