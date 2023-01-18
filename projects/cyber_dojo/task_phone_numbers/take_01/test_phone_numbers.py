import pytest

from phone_numbers import PhoneNumbers


class TestPhoneNumbers:
    def test_is_consistent__false(self):
        phone_numbers = [
            'Bob 91 12 54 26',
            'Alice 97 625 992',
            'Emergency 911',
            ]
        result = PhoneNumbers.is_consistent(phone_numbers)
        expected = False
        assert result == expected

    def test_is_consistent__true(self):
        phone_numbers = [
            'Virgilio Theone 03217 981-017',
            'Clara Wedel 064398 681 004',
            'Ursula Hardrick 00156-20607 09',
            'Alonso Schroyer 04760206-585',
            'Maria Pukhalskaya 0056-146 0726',
            'Yoshiko 06235-742-1964',
            'Joan Pinol  070247-9 03',
            'Claud Bardon 0284-43-9384',
            'Ervin Kennemore 08790 8069715',
            'Emergency 911',
            'Shelby Lynne 064 07651 89',
            'Winford Hagwood 06517-570 26-89',
            'Blythe Milby 08627309 831',
            'Cherry Font 01724584-6 32',
            'Ruggero Bussmann 09310-502-38 4',
            'Briana Letterman 015274-0464-5',
            ]
        result = PhoneNumbers.is_consistent(phone_numbers)
        expected = True
        assert result == expected

    def test_is_consistent__empty(self):
        phone_numbers = []
        result = PhoneNumbers.is_consistent(phone_numbers)
        expected = False
        assert result == expected

    @pytest.mark.parametrize('phone_numbers, expected', [
        (['Bob 91 12 54 26', 'Alice 97 625 992'], {'91125426', '97625992'}),
        (['Emergency 911', 'Maria Pukhalskaya 0056-146 0726'], {'911', '00561460726'}),
        ])
    def test_get_digits(self, phone_numbers, expected):
        result = PhoneNumbers.get_digits(phone_numbers)
        assert result == expected
