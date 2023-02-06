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

    @pytest.mark.parametrize('item, coins, expected', [
        ('chips',
            [(24.257, 1.956, 5.67),
             (24.257, 1.956, 5.67),
             (24.257, 1.956, 5.67),
             (24.257, 1.956, 5.67),
             ],
            (True, 0.5)
         ),
        ('cola',
            [(24.257, 1.956, 5.67),
             (24.257, 1.956, 5.67),
             (24.257, 1.956, 5.67),
             (24.257, 1.956, 5.67),
             (24.257, 1.956, 5.67),
             (24.257, 1.956, 5.67),
             (24.257, 1.956, 5.67),
             (17.91, 1.35, 2.268),
             ],
            (True, 0.85)
         ),
        ])
    def test_process_order(self, stock_items, item, coins, expected):
        vending_machine = VendingMachine()
        vending_machine.add_items(stock_items)
        result = vending_machine.process_order(item, coins)
        assert result == expected

    @pytest.mark.parametrize('item, expected', [
        (('chips', []), 'SOLD OUT'),
        (('candy', []), 3),
        ])
    def test_after_process_order_stock_will_be_updated(self, stock_items, item, expected):
        vending_machine = VendingMachine()
        vending_machine.add_items(stock_items)
        vending_machine.process_order(*item)
        result = vending_machine.get_item_qty(item[0])
        assert result == expected

    def test_process_order__not_enough_stock(self, stock_items):
        items_n_expected = [
            ({'name': 'chips', 'price': []}, 'SOLD OUT'),
            ({'name': 'cola', 'price': []}, 1),
            ({'name': 'cola', 'price': []}, 'SOLD OUT'),
            ]
        vending_machine = VendingMachine()
        vending_machine.add_items(stock_items)

        for item, expected in items_n_expected:
            vending_machine.process_order(*item.values())
            result = vending_machine.get_item_qty(item['name'])
            assert result == expected

    def test_process_order__happy_path_states(self, stock_items):
        vending_machine = VendingMachine()
        assert vending_machine.state == VendingMachineState.CHOOSE_ITEM

        vending_machine.add_items(stock_items)
        vending_machine.choose_item('candy')
        assert vending_machine.state == VendingMachineState.INSERT_MONEY

        vending_machine.process_coins_value()
        assert vending_machine.state == VendingMachineState.PUSH_CHANGE

        vending_machine.push_change()
        assert vending_machine.state == VendingMachineState.PUSH_PRODUCT

        vending_machine.push_product()
        assert vending_machine.state == VendingMachineState.SALE_PROCESSED

    @pytest.mark.parametrize('coin_stats, expected', [
        ((17.91, 1.35, 2.268), 0.10),
        ((21.21, 1.95, 5), 0.05),
        ((24.257, 1.956, 5.67), 0.25),
        ((22, 1.95, 5), 0),
        ((0, 0, 0), 0),
        ])
    def test_insert_coin__calc_value(self, stock_items, coin_stats, expected):
        vending_machine = VendingMachine()
        vending_machine.insert_coin(*coin_stats)
        vending_machine.process_coins_value()
        result = vending_machine.money
        assert result == expected

    def test_get_coins_value(self):
        coins = [
            (17.91, 1.35, 2.268),
            (21.21, 1.95, 5),
            (24.257, 1.956, 5.67),
            (21.21, 1.95, 5),
            (22, 1.95, 5),
            ]
        vending_machine = VendingMachine()
        for coin in coins:
            vending_machine.insert_coin(*coin)
        vending_machine.process_coins_value()
        result = vending_machine.money
        expected = 0.45
        assert result == expected
