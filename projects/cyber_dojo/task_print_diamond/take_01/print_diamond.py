START_LETTER = 'A'
SPACES = [0] + list(range(1, 101, 2))


class PrintDiamond:
    def __init__(self, letter):
        self.letter = letter.upper()
        self.diamond = []

        if not self._is_input_valid():
            return
        if self.letter == START_LETTER:
            self.diamond = [START_LETTER]
            return

        self._process()

    def _is_input_valid(self):
        if any((not self.letter,
                not isinstance(self.letter, str),
                len(self.letter) > 1,
                self.letter < 'A',
                self.letter > 'Z')):
            return False
        return True

    def _add_lines_until_middle_of_diamond(self, spaces, len_to_start_letter):
        for i in range(1, len_to_start_letter + 1):
            ch = chr(i + ord(START_LETTER))
            additional_spaces = SPACES[i]
            self.diamond += [f"{ch}{' ' * additional_spaces}{ch}".center(spaces)]

    def _process(self):
        len_to_start_letter = ord(self.letter) - ord(START_LETTER)
        spaces = SPACES[len_to_start_letter + 1]

        # Add first line of the diamond
        self.diamond += [START_LETTER.center(spaces)]

        self._add_lines_until_middle_of_diamond(spaces, len_to_start_letter)

        # Add mirrored lines to complete the diamond
        self.diamond += [row for row in reversed(self.diamond[:-1])]

    def __str__(self):
        return '\n'.join(self.diamond)

    def __repr__(self):
        return f"{self.__class__.__name__}(" \
               f"'{self.letter}')"
