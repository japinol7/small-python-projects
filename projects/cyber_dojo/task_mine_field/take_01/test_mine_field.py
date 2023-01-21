from mine_field import MineField


class TestMineField:
    def test_resolve_1(self):
        board = '3 4\n'\
                '*...\n'\
                '..*.\n'\
                '....'
        result = MineField(board).resolve()
        expected = '*211\n'\
                   '12*1\n'\
                   '0111'
        assert result == expected

    def test_resolve_2(self):
        board = '5 4\n'\
                '*...\n'\
                '..*.\n'\
                '...*\n' \
                '....\n' \
                '.*..'
        result = MineField(board).resolve()
        expected = '*211\n'\
                   '12*2\n'\
                   '012*\n' \
                   '1121\n' \
                   '1*10'
        assert result == expected
