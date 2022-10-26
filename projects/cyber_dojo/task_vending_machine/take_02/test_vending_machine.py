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

    def test_add_items__some_exist(self, stock_items):
        vending_machine = VendingMachine()
        initial_items = [
            {'name': 'candy', 'qty': 1, 'price': 0.65},
            {'name': 'cola', 'qty': 10, 'price': 0.65},
            {'name': 'sprite', 'qty': 2, 'price': 0.70},
            ]
        vending_machine.add_items(initial_items)
        vending_machine.add_items(stock_items)
        result = vending_machine.items
        expected = {
            'candy': {'name': 'candy', 'price': 0.65, 'qty': 5},
            'chips': {'name': 'chips', 'price': 0.5, 'qty': 1},
            'cola': {'name': 'cola', 'price': 1, 'qty': 12},
            'sprite': {'name': 'sprite', 'qty': 2, 'price': 0.70},
            }
        assert result == expected

    @pytest.mark.parametrize('item, expected', [
        (('chips', 1), (True, 0.5)),
        (('cola', 2), (True, 1)),
        ])
    def test_process_order(self, stock_items, item, expected):
        vending_machine = VendingMachine()
        vending_machine.add_items(stock_items)
        result = vending_machine.process_order(*item)
        assert result == expected
