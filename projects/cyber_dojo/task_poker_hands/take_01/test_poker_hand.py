import pytest

from poker_hand import PokerHand


class TestPokerHand:
    @pytest.mark.parametrize('card, value', [
        ('JD', 11),
        ('AD', 14),
        ('7C', 7),
        ('10C', 10),
        ])
    def test_value_card(self, card, value):
        result = PokerHand.value_card(card)
        expected = value
        assert result == expected

    @pytest.mark.parametrize('cards, values_counter', [
        (['2C', '3D', '4S', '5H', '2D'],
         {2: 2, 3: 1, 4: 1, 5: 1}),
        ])
    def test_values_counter(self, cards, values_counter):
        hand = PokerHand(cards, setup=True)
        result = hand.values_counter
        expected = values_counter
        assert result == expected

    @pytest.mark.parametrize('cards, value, card_count', [
        (['2C', '3D', '4S', '5H', '2D'], 2, 2),
        (['2C', '3D', '4S', '5H', '2D'], 3, 0),
        (['2C', '3D', '4S', '5H', '2D'], 4, 0),
        (['5S', '4C', 'AD', '4S', '4H'], 3, 4),
        (['5S', '4C', 'AD', '4S', '4H'], 4, 0),
        (['5S', '4C', 'AD', '4S', '4H'], 2, 0),
        ])
    def test_card_count(self, cards, value, card_count):
        hand = PokerHand(cards, setup=True)
        result = hand.find_value_repeated_n_times(value)
        expected = card_count
        assert result == expected

    @pytest.mark.parametrize('cards, is_flush', [
        (['2C', '3D', '4S', '5H', '2D'], False),
        (['5S', '4C', 'AD', '4S', '4H'], False),
        (['AC', '5C', '10C', '7C', '3C'], True),
        (['AS', '10S', 'QS', 'KS', 'JS'], True),
        ])
    def test_is_flush(self, cards, is_flush):
        hand = PokerHand(cards)
        result = hand.is_flush()
        expected = is_flush
        assert result == expected

    @pytest.mark.parametrize('cards, straight_high_card', [
        (['2C', '3D', '4S', '5H', '2D'], None),
        (['5S', '4C', 'AD', '4S', '4H'], None),
        (['AC', '5C', '10C', '7C', '3C'], None),
        (['3H', '7H', '6S', '4D', '5S'], 7),
        (['AS', '10S', 'QS', 'KS', 'JS'], 14),
        ])
    def test_straight_high_card(self, cards, straight_high_card):
        hand = PokerHand(cards)
        result = hand.get_straight_high_card()
        expected = straight_high_card
        assert result == expected

    @pytest.mark.parametrize('cards, rank', [
        (['2C', '3H', '4S', '8C', '7H'], 8),
        (['2H', '3D', '5S', '9C', 'KD'], 13),
        (['AC', '5C', '10C', '7C', '3S'], 14),
        (['2C', '3D', '4S', '5H', '2D'], 101),
        (['2C', '3D', '4S', '3H', '2D'], 102),
        (['5S', '4C', 'AD', '4S', '4H'], 103),
        (['3H', '7H', '6S', '4D', '5S'], 104),
        (['AC', '5C', '10C', '7C', '3C'], 105),
        (['5C', '8D', '5H', '8S', '8H'], 106),
        (['3D', '7H', '7S', '7C', '7D'], 107),
        (['AS', '10S', 'QS', 'KS', 'JS'], 108),
        ])
    def test_rank(self, cards, rank):
        hand = PokerHand(cards, setup=True)
        result = hand.get_rank()
        expected = rank
        assert result == expected

    @pytest.mark.parametrize('rank, rank_name', [
        (14, 'high card: Ace'),
        (11, 'high card: J'),
        (7, 'high card: 7'),
        (101, 'pair'),
        (102, 'two pairs'),
        (103, 'three of a kind'),
        (104, 'straight'),
        (105, 'flush'),
        (106, 'full house'),
        (107, 'four of a kind'),
        (108, 'straight flush'),
        ])
    def test_rank_name(self, rank, rank_name):
        result = PokerHand.get_rank_name(rank)
        expected = rank_name
        assert result == expected
