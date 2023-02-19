import pytest

from item import Item, ItemException


class TestItem:
    @pytest.mark.parametrize('name, stock, price, expected', [
        ('candy', 4, 0.65, "Item(name='candy', price=0.65, stock=4)"),
        ('chips', 1, 0.5, "Item(name='chips', price=0.5, stock=1)"),
        ('cola', 2, 1, "Item(name='cola', price=1, stock=2)"),
        ]
                             )
    def test_create_item(self, name, stock, price, expected):
        result = Item(name, price=price, stock=stock)
        assert repr(result) == expected

    def test_create_item_with_negative_stock_should_raise_exception(self):
        with pytest.raises(ItemException):
            Item(name='candy', price=0.65, stock=-1)

    def test_change_stock_with_negative_value_should_raise_exception(self):
        item = Item(name='candy', price=0.65, stock=2)
        with pytest.raises(ItemException):
            item.stock = -1

    def test_decrease_stock_when_it_is_zero_should_raise_exception(self):
        item = Item(name='candy', price=0.65, stock=0)
        with pytest.raises(ItemException):
            item.decrease_stock()

