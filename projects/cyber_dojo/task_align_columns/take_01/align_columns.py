from enum import Enum
from itertools import zip_longest


class ColumnAlignment(str, Enum):
    Center = '^'
    Left = '<'
    Right = '>'


class AlignColumns:
    @staticmethod
    def align_columns(text, alignment):
        if not text:
            return ''

        parts = [line.rstrip('$').split('$') for line in text.splitlines()]
        widths = [max(len(word) for word in col)
                  for col in zip_longest(*parts, fillvalue='')]

        res = []
        for line in parts:
            res += [' '.join(f'{word:{alignment.value}{width_}}' for width_, word in zip(widths, line))]

        return ''.join(res)
