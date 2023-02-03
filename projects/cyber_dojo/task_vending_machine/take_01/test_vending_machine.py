import pytest

from vending_machine import VendingMachine, VendingMachineState


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

    @pytest.mark.parametrize('item, expected', [
        (('chips', 1), 'SOLD OUT'),
        (('candy', 2), 3),
        ])
    def test_after_process_order_stock_will_be_updated(self, stock_items, item, expected):
        vending_machine = VendingMachine()
        vending_machine.add_items(stock_items)
        vending_machine.process_order(*item)
        result = vending_machine.get_item_qty(item[0])
        assert result == expected

    def test_process_order__not_enough_stock(self, stock_items):
        items_n_expected = [
            ({'name': 'chips', 'price': 0.5}, 'SOLD OUT'),
            ({'name': 'cola', 'price': 1}, 1),
            ({'name': 'cola', 'price': 1}, 'SOLD OUT'),
            ]
        vending_machine = VendingMachine()
        vending_machine.add_items(stock_items)

        for item, expected in items_n_expected:
            vending_machine.process_order(*item.values())
            result = vending_machine.get_item_qty(item['name'])
            assert result == expected

    def test_process_order__simple_states(self, stock_items):
        vending_machine = VendingMachine()
        assert vending_machine.state == VendingMachineState.CHOOSE_ITEM

        vending_machine.add_items(stock_items)
        item = 'candy', 2
        vending_machine.choose_item(item[0])
        assert vending_machine.state == VendingMachineState.INSERT_MONEY

        vending_machine.insert_money(item[1])
        assert vending_machine.state == VendingMachineState.SALE_PROCESSED
