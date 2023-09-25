START_LETTER = 'A'
EMPTY_CELL = ' '


class Diamond:

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

    def _add_lines_until_middle_of_diamond(self, size):
        current_letter_ord = ord(START_LETTER) + 1

        out_cell_count = size - 2
        center_cell_count = 1
        for _ in range(1, size):
            self.diamond += [
                f"{EMPTY_CELL * out_cell_count}"
                f"{chr(current_letter_ord)}"
                f"{EMPTY_CELL * center_cell_count}"
                f"{chr(current_letter_ord)}"
                f"{EMPTY_CELL * out_cell_count}"
                ]
            current_letter_ord += 1
            out_cell_count -= 1
            center_cell_count += 2

    def _process(self):
        letter_ord_distance_to_a = ord(self.letter) - ord(START_LETTER)
        size = letter_ord_distance_to_a + 1

        # Add first line of the diamond
        self.diamond += [EMPTY_CELL * (size - 1) + 'A' + EMPTY_CELL * (size - 1)]

        self._add_lines_until_middle_of_diamond(size)

        # Add mirrored lines to complete the diamond
        self.diamond += [row for row in reversed(self.diamond[:-1])]

    def print(self):
        return '\n'.join(self.diamond)
