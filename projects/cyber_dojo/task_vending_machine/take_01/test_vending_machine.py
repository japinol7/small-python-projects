import pytest

from vending_machine import VendingMachine


class TestVendingMachine:
    def test_add_items(self, stock_items):
        vending_machine = VendingMachine()
        vending_machine.add_items(stock_items)
        result = vending_machine.items
        expected = {
            'candy': {'name': 'candy', 'price': 0.65, 'qty': 4},
            'chips': {'name': 'chips', 'price': 0.5, 'qty': 1},
            'cola': {'name': 'cola', 'price': 1, 'qty': 2}
            }
        assert result == expected
