import pytest

from poker_hands import PokerHands, PokerHandsException
from poker_hand import PokerHand


class TestPokerHands:
    @pytest.mark.parametrize('hand_1, hand_2, winner_expected', [
        (
            PokerHand(['2H', '3D', '5S', '9C', 'KD'], name='Black', setup=True),
            PokerHand(['2C', '3H', '4S', '8C', 'AH'], name='White', setup=True),
            'White',
         ),
        (
            PokerHand(['2H', '4S', '4C', '2D', '4H'], name='Black', setup=True),
            PokerHand(['2S', '8S', 'AS', 'QS', '3S'], name='White', setup=True),
            'Black',
        ),
        (
            PokerHand(['2H', '3D', '5S', '9C', '8D'], name='Black', setup=True),
            PokerHand(['2C', '3H', '4S', '8C', '7H'], name='White', setup=True),
            'Black',
        ),
        (
            PokerHand(['2H', '3D', '5S', '9C', 'KD'], name='Black', setup=True),
            PokerHand(['2D', '3H', '5C', '9S', 'KH'], name='White', setup=True),
            None,
        ),
        (
            PokerHand(['AC', '5C', '10C', '7C', '3S'], name='Black', setup=True),
            PokerHand(['5C', '8D', '5H', '8S', '8H'], name='White', setup=True),
            'White',
         ),
        (
            PokerHand(['3D', '7H', '7S', '7C', '7D'], name='Black', setup=True),
            PokerHand(['2C', '3D', '4S', '5H', '2D'], name='White', setup=True),
            'Black',
        ),
        (
            PokerHand(['2C', '3D', '4S', '5H', '2D'], name='Black', setup=True),
            PokerHand(['2C', '3D', '4S', '5H', '2D'], name='White', setup=True),
            None,
        ),
        (
            PokerHand(['3H', '7H', '6S', '4D', '5S'], name='Black', setup=True),
            PokerHand(['5C', '8D', '5H', '8S', '8H'], name='White', setup=True),
            'White',
        ),
        ])
    def test_get_winner(self, hand_1, hand_2, winner_expected):
        poker_hands = PokerHands([hand_1, hand_2])
        winner = poker_hands.get_winner()
        result = winner.name if winner else None
        expected = winner_expected
        assert result == expected
        hand_1_rank = hand_1.get_rank()
        hand_2_rank = hand_2.get_rank()
        print("Output: \n------------------------\n"
              f"Poker Hands:\n"
              f"hand_1: {hand_1}\n"
              f"hand_2: {hand_2}\n"
              "--------\n"
              f"winner: {winner if winner else 'Tie'}\n"
              "--------\n"
              f"hand_1 rank: {hand_1_rank}\n"
              f"hand_2 rank: {hand_2_rank}\n"
              f"hand_1 rank name: {PokerHand.get_rank_name(hand_1_rank)}\n"
              f"hand_2 rank name: {PokerHand.get_rank_name(hand_2_rank)}\n"
              )

    def test_raise_exception(self):
        with pytest.raises(PokerHandsException):
            PokerHands([
                PokerHand(['2H', '3D', '5S', '9C', 'KD'], name='Black'),
                PokerHand(['5C', '8D', '5H', '8S', '8H'], name='White'),
                PokerHand(['2S', '8S', 'AS', 'QS', '3S'], name='White'),
            ])
