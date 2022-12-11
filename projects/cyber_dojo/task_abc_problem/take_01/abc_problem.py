from collections import Counter

BLOCKS = (
    ('B', 'O'),
    ('X', 'K'),
    ('D', 'Q'),
    ('C', 'P'),
    ('N', 'A'),
    ('G', 'T'),
    ('R', 'E'),
    ('T', 'G'),
    ('Q', 'D'),
    ('F', 'S'),
    ('J', 'W'),
    ('H', 'U'),
    ('V', 'I'),
    ('A', 'N'),
    ('O', 'B'),
    ('E', 'R'),
    ('F', 'S'),
    ('L', 'Y'),
    ('P', 'C'),
    ('Z', 'M'),
    )


class ABCProblem:
    @staticmethod
    def can_make_word(word):
        if not word:
            return False

        letters_count = Counter(x for x, y in BLOCKS)
        letters_count.update(y for x, y in BLOCKS)
        word = word.upper()

        for ch in word:
            if ch not in letters_count or letters_count[ch] < 1:
                return False
            letters_count[ch] -= 1
            # Remove also the other letter of the block, so it cannot be used the same block twice
            for x, y in BLOCKS:
                if x == ch:
                    letters_count[y] -= 1
                    break
                elif y == ch:
                    letters_count[x] -= 1
                    break
        return True
