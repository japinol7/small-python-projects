import pytest

from harry_potter import Item, ShoppingBasket


@pytest.mark.parametrize('shopping_items, expected', [
    ([Item('harry_potter_book_01', 1),
      ], 8),
    ([Item('harry_potter_book_02', 3),
      ], 24),
    ([Item('harry_potter_book_01', 1),
      Item('harry_potter_book_02', 1),
      ], 15.2),
    ([Item('harry_potter_book_01', 1),
      Item('harry_potter_book_02', 1),
      Item('harry_potter_book_04', 1),
      ], 21.6),
    ([Item('harry_potter_book_01', 1),
      Item('harry_potter_book_02', 1),
      Item('harry_potter_book_04', 1),
      Item('harry_potter_book_05', 1),
      ], 25.6),
    ([Item('harry_potter_book_01', 1),
      Item('harry_potter_book_02', 1),
      Item('harry_potter_book_03', 1),
      Item('harry_potter_book_04', 1),
      Item('harry_potter_book_05', 1),
      ], 30),
    ([Item('harry_potter_book_02', 1),
      Item('harry_potter_book_04', 1),
      Item('harry_potter_book_05', 2),
      Item('harry_potter_book_07', 1),
      ], 33.6),
    ([Item('harry_potter_book_03', 2),
      Item('harry_potter_book_04', 2),
      Item('harry_potter_book_05', 2),
      ], 43.2),
    ([Item('harry_potter_book_01', 2),
      Item('harry_potter_book_02', 2),
      Item('harry_potter_book_03', 2),
      Item('harry_potter_book_04', 1),
      Item('harry_potter_book_05', 1),
      ], 51.20),
    ([], 0),
    ])
def test_shopping_basket_get_price(shopping_items, expected):
    result = ShoppingBasket(shopping_items).get_price()
    assert result == expected
