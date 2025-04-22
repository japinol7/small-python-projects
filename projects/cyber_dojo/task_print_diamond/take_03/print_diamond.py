SEP = ' '


class PrintDiamond:
    def __init__(self, letter):
        self.letter = letter
        self.result = ''

        if not isinstance(self.letter, str):
            self.result = ''
            raise ValueError(
                "the letter parameter must be a str of one character")

        self.letter = self.letter.strip().upper()
        if not self._check_sad_paths():
            return

        self._process()

    def _check_sad_paths(self):
        if not self.letter:
            self.result = ''
            return False

        if len(self.letter) > 1:
            self.result = ''
            return False

        if ord(self.letter) > ord('Z'):
            self.result = ''
            return False

        return True

    def _process(self):
        if self.letter == 'A':
            self.result = 'A'
            return

        rows_half_n = ord(self.letter) - ord('A')
        cols_n = rows_half_n * 2 + 1
        rows_first_half = []
        rows = []

        # Add first half rows
        rows_first_half += ['A'.center(cols_n, SEP)]
        spcs = 1
        for i in range(1, rows_half_n):
            ch = chr(i + ord('A'))
            rows_first_half += [
                f"{ch}{' ' * spcs}{ch}".center(cols_n, SEP)
                ]
            spcs += 2
        rows += rows_first_half

        # Add the middle row
        ch = chr(rows_half_n + ord('A'))
        rows += [f"{ch}{SEP * spcs}{ch}"]

        # Add second half rows
        rows += rows_first_half[::-1]

        self.result = '\n'.join(rows)

    def __str__(self):
        return self.result

    def __repr__(self):
        return f"{self.__class__.__name__}(" \
               f"'{self.letter}')"
