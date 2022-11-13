from collections import Counter

CARD_VALUES = {
    'T': 10,
    'J': 11,
    'Q': 12,
    'K': 13,
    'A': 14,
    }

RANK_NAMES = {
    101: 'pair',
    102: 'two pairs',
    103: 'three of a kind',
    104: 'straight',
    105: 'flush',
    106: 'full house',
    107: 'four of a kind',
    108: 'straight flush',
    14: 'high card: Ace',
    13: 'high card: K',
    12: 'high card: Q',
    11: 'high card: J',
    10: 'high card: 10',
    9: 'high card: 9',
    8: 'high card: 8',
    7: 'high card: 7',
    6: 'high card: 6',
    5: 'high card: 5',
    4: 'high card: 4',
    3: 'high card: 3',
    2: 'high card: 2',
    }


class PokerHand:
    def __init__(self, cards, name=None, setup=False):
        self.cards = cards
        self.name = name
        self.values_counter = None
        if setup:
            self.setup()

    def setup(self):
        if self.values_counter:
            return
        self.values_counter = Counter([self.value_card(card) for card in self.cards])

    @staticmethod
    def get_suit(card):
        return card[-1]

    @staticmethod
    def value_card(card):
        res = CARD_VALUES.get(card[0])
        if not res:
            res = int(card[0: -1])
        return res

    def find_value_repeated_n_times(self, times_repeated, exclude_value=0):
        """Finds first value that is repeated times_repeated times
        with the exclusion of the exclude_value value.
        """
        for value in self.values_counter:
            if value == exclude_value:
                continue
            if self.values_counter[value] == times_repeated:
                return value
        return 0

    def is_flush(self):
        return all((self.get_suit(card) == self.get_suit(self.cards[0]) for card in self.cards[1:]))

    def get_straight_high_card(self):
        card_distinct_values = sorted(list(set((self.value_card(card) for card in self.cards))))
        if len(card_distinct_values) < 5:
            return None
        max_card = max(card_distinct_values)
        if card_distinct_values == list(range(min(card_distinct_values), max_card + 1)):
            return max_card
        return None

    def get_rank(self):
        if self.get_straight_high_card() and self.is_flush():
            return 108
        if self.find_value_repeated_n_times(4):
            return 107
        if self.find_value_repeated_n_times(3) and self.find_value_repeated_n_times(2):
            return 106
        if self.is_flush():
            return 105
        if self.get_straight_high_card():
            return 104
        if self.find_value_repeated_n_times(3):
            return 103
        pair_value = self.find_value_repeated_n_times(2)
        if pair_value:
            if self.find_value_repeated_n_times(2, exclude_value=pair_value):
                return 102
            return 101
        return max(self.values_counter)

    @staticmethod
    def get_rank_name(rank):
        return RANK_NAMES[rank]

    def __str__(self):
        return (f"name: {self.name!r}, "
                f"cards: {self.cards!r}")

    def __repr__(self):
        return (f"{self.__class__.__name__}("
                f"{self.cards!r}, "
                f"name={self.name!r})")
