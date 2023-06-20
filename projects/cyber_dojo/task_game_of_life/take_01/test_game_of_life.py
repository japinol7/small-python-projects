import pytest

from game_of_life import GameOfLife, GameOfLifeException

TEST_CASE_1 = (
    4, 8,
    '........\n'
    '....*...\n'
    '...**...\n'
    '.....*..',
    )

TEST_CASE_1_EXPECTED = (
    4, 8,
    '........\n'
    '...**...\n'
    '...***..\n'
    '....*...',
    )

TEST_CASE_2 = (
    5, 8,
    '........\n'
    '...**...\n'
    '.*****..\n'
    '........\n'
    '........',
    )

TEST_CASE_2_EXPECTED = (
    5, 8,
    '........\n'
    '.....*..\n'
    '..*..*..\n'
    '..***...\n'
    '........',
    )


class TestGameOfLife:
    @pytest.mark.parametrize('input_vals', [
        (0, 0, ''),
        (4, 8, ''),
        (4, 0, '........'),
        ])
    def test_calc_next_generation__invalid_input_raise_exception(self, input_vals):
        with pytest.raises(GameOfLifeException):
            GameOfLife(*input_vals)

    @pytest.mark.parametrize('row, col, grid_data, expected', [
        (1, 4, TEST_CASE_1, 2),
        (1, 3, TEST_CASE_2, 4),
        (1, 4, TEST_CASE_2, 4),
        ])
    def test_count_neighbours(self, row, col, grid_data, expected):
        result = GameOfLife(*grid_data).count_neighbours(row, col)
        assert result == expected

    @pytest.mark.parametrize('input_vals, expected', [
        (TEST_CASE_1, TEST_CASE_1_EXPECTED[2]),
        (TEST_CASE_2, TEST_CASE_2_EXPECTED[2]),
        ])
    def test_calc_next_generation(self, input_vals, expected):
        result = GameOfLife(*input_vals).calc_next_generation()
        assert result == expected
