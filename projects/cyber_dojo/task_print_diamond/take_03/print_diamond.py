SEP = ' '


class PrintDiamond:
    def __init__(self, letter):
        self.letter = letter
        self.output = ''

        if not isinstance(self.letter, str):
            self.result = ''
            raise ValueError(
                "the letter parameter must be a str of one character")

        self.letter = self.letter.strip().upper()

        if not self._validate_input():
            return

        self._process()

    def _validate_input(self):
        if not self.letter or len(self.letter) > 1:
            return False

        if ord(self.letter) < ord('A') or ord(self.letter) > ord('Z'):
            return False

        return True

    def _process(self):
        if self.letter == 'A':
            self.output = 'A'
            return

        rows_first_half_n = ord(self.letter) - ord('A')
        rows_n = rows_first_half_n * 2 + 1
        rows = []
        rows_first_half = []
        rows_second_half = []

        # Populate first half
        rows_first_half += ['A'.center(rows_n, SEP)]
        sep_n = 1
        ord_ch = ord('A')
        for ord_ch in range(ord('B'),  ord(self.letter)):
            ch = chr(ord_ch)
            rows_first_half += [
                f"{ch}{SEP * sep_n}{ch}".center(rows_n, SEP)
                ]
            sep_n += 2

        # Populate middle half
        ord_ch += 1
        ch = chr(ord_ch)
        rows_middle_half = [
            f"{ch}{SEP * sep_n}{ch}".center(rows_n, SEP)
            ]

        # Populate second half
        rows_second_half += list(reversed(rows_first_half))

        rows += rows_first_half + rows_middle_half + rows_second_half
        self.output = '\n'.join(rows)

    def __str__(self):
        return self.output

    def __repr__(self):
        return f"{self.__class__.__name__}(" \
               f"'{self.letter}')"
