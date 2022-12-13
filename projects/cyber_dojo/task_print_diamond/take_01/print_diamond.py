START_LETTER = 'A'
SPACES = [0] + list(range(1, 101, 2))


class PrintDiamond:
    def __init__(self, letter):
        self.letter = letter.upper()
        self.diamond = []

        if any((not self.letter,
                not isinstance(self.letter, str),
                len(self.letter) > 1,
                self.letter < 'A',
                self.letter > 'Z')):
            return
        if self.letter == START_LETTER:
            self.diamond += [START_LETTER]
            return

        self._process()

    def _process(self):
        len_to_start_letter = ord(self.letter) - ord(START_LETTER)
        spaces = SPACES[len_to_start_letter + 1]
        self.diamond += [START_LETTER.center(spaces)]
        # Add lines until the middle of the diamond
        for i in range(1, len_to_start_letter + 1):
            ch = chr(i + ord(START_LETTER))
            additional_spaces = SPACES[i]
            self.diamond += [f"{ch}{' ' * additional_spaces}{ch}".center(spaces)]
        # Add mirrored lines to complete de diamond
        for line in reversed(self.diamond[:-1]):
            self.diamond += [line]

    def __str__(self):
        return '\n'.join(self.diamond)

    def __repr__(self):
        return f"{self.__class__.__name__}(" \
               f"'{self.letter}')"
