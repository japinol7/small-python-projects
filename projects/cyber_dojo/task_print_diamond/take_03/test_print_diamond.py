import pytest

from print_diamond import PrintDiamond


class TestPrintDiamond:
    @pytest.mark.parametrize('letter, expected', [
        ('', ''),
        (' ', ''),
        ('ñ', ''),
        ('FG', ''),
        ])
    def test_print_diamond_empty(self, letter, expected):
        result = str(PrintDiamond(letter))
        assert result == expected

    def test_print_diamond_a(self):
        result = str(PrintDiamond('A'))
        expected = 'A'
        assert result == expected

    def test_print_diamond_b(self):
        result = str(PrintDiamond('B'))
        expected = ' A \n' \
                   'B B\n' \
                   ' A '
        assert result == expected

    def test_print_diamond_c(self):
        result = str(PrintDiamond('C'))
        expected = '  A  \n' \
                   ' B B \n' \
                   'C   C\n' \
                   ' B B \n' \
                   '  A  '
        assert result == expected

    def test_print_diamond_d(self):
        result = str(PrintDiamond('D'))
        expected = '   A   \n' \
                   '  B B  \n' \
                   ' C   C \n' \
                   'D     D\n' \
                   ' C   C \n' \
                   '  B B  \n' \
                   '   A   '
        assert result == expected

    def test_print_diamond_f(self):
        result = str(PrintDiamond('F'))
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
        result = str(PrintDiamond('E'))
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
