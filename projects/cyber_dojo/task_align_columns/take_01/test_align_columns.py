import pytest

from align_columns import AlignColumns
from align_columns import ColumnAlignment

TEXT = """Given$a$text$file$of$many$lines,$where$fields$within$a$line$
are$delineated$by$a$single$'dollar'$character,$write$a$program
that$aligns$each$column$of$fields$by$ensuring$that$words$in$each$
column$are$separated$by$at$least$one$space."""

EXPECTED_ALIGN_VALS = {
    ColumnAlignment.LEFT:
        "Given  a          text      file   of     many     lines,     where    fields within  a  line\n"
        "are    delineated by        a      single 'dollar' character, write    a      program\n"
        "that   aligns     each      column of     fields   by         ensuring that   words   in each\n"
        "column are        separated by     at     least    one        space.  ",
    ColumnAlignment.RIGHT:
        " Given          a      text   file     of     many     lines,    where fields  within  a line\n"
        "   are delineated        by      a single 'dollar' character,    write      a program\n"
        "  that     aligns      each column     of   fields         by ensuring   that   words in each\n"
        "column        are separated     by     at    least        one   space.",
    ColumnAlignment.CENTER:
        "Given      a        text     file    of     many     lines,    where   fields within  a  line\n"
        " are   delineated    by       a    single 'dollar' character,  write     a    program\n"
        " that    aligns     each    column   of    fields      by     ensuring  that   words  in each\n"
        "column    are     separated   by     at    least      one      space. ",
    }


class TestAlignColumns:
    @pytest.mark.parametrize('alignment, expected', [
        (alignment, expected) for alignment, expected in EXPECTED_ALIGN_VALS.items()]
        )
    def test_align_columns(self, alignment, expected):
        result = AlignColumns.align_columns(TEXT, alignment)
        assert result == expected

    def test_align_columns_empty(self):
        result = AlignColumns.align_columns('', ColumnAlignment.LEFT)
        expected = ''
        assert result == expected
