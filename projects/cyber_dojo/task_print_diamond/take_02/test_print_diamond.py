import pytest

from print_diamond import Diamond


class TestDiamond:
    @pytest.mark.parametrize('letter, expected', [
        ('', ''),
        (' ', ''),
        ('á', ''),
        ('>', ''),
        ('ABC', ''),
        ])
    def test_print_diamond_empty(self, letter, expected):
        result = Diamond(letter).print()
        assert result == expected

    def test_diamond_for_a(self):
        result = Diamond('A').print()
        assert result == 'A'

    def test_diamond_for_b(self):
        result = Diamond('B').print()
        expected = ' A \n' \
                   'B B\n' \
                   ' A '
        assert result == expected

    def test_diamond_for_c(self):
        result = Diamond('C').print()
        expected = '  A  \n' \
                   ' B B \n' \
                   'C   C\n' \
                   ' B B \n' \
                   '  A  '
        assert result == expected

    def test_diamond_for_d(self):
        result = Diamond('D').print()
        expected = '   A   \n' \
                   '  B B  \n' \
                   ' C   C \n' \
                   'D     D\n' \
                   ' C   C \n' \
                   '  B B  \n' \
                   '   A   '
        assert result == expected

    def test_diamond_for_f(self):
        result = Diamond('F').print()
        expected = '     A     \n' \
                   '    B B    \n' \
                   '   C   C   \n' \
                   '  D     D  \n' \
                   ' E       E \n' \
                   'F         F\n' \
                   ' E       E \n' \
                   '  D     D  \n' \
                   '   C   C   \n' \
                   '    B B    \n' \
                   '     A     '
        assert result == expected

    def test_print_diamond_e_and_output(self):
        result = Diamond('E').print()
        expected = '    A    \n' \
                   '   B B   \n' \
                   '  C   C  \n' \
                   ' D     D \n' \
                   'E       E\n' \
                   ' D     D \n' \
                   '  C   C  \n' \
                   '   B B   \n' \
                   '    A    '
        assert result == expected
        print(f"\nOutput:\n{result}")
