class PokerHandsException(Exception):
    pass


class PokerHands:
    def __init__(self, hands):
        if len(hands) != 2:
            raise PokerHandsException("Input error: This implementation only considers "
                                      f"games with two hands. Value: {hands}")
        self.hands = hands

    def get_winner(self):
        max_rank = max(self.hands, key=lambda x: x.get_rank())
        min_rank = min(self.hands, key=lambda x: x.get_rank())
        return max_rank if max_rank != min_rank else None
