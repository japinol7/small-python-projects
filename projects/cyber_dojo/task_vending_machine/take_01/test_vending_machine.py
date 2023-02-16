import pytest

from coin import Coin
from vending_machine import VendingMachineState


class TestVendingMachine:
    def test_add_items(self, vending_machine_with_stock):
        vending_machine = vending_machine_with_stock
        result = vending_machine.items
        expected = {
            'candy': {'name': 'candy', 'price': 0.65, 'qty': 4},
            'chips': {'name': 'chips', 'price': 0.5, 'qty': 1},
            'cola': {'name': 'cola', 'price': 1, 'qty': 2}
            }
        assert result == expected

    def test_add_items__some_exist(self, vending_machine, stock_items):
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

    def test_process_order__happy_path_states(self, vending_machine, stock_items):
        assert vending_machine.state == VendingMachineState.INSERT_MONEY
        vending_machine.add_items(stock_items)

        vending_machine.insert_coin(17.91, 1.35, 2.268)
        vending_machine.insert_coin(21.21, 1.95, 5)
        vending_machine.insert_coin(24.257, 1.956, 5.67)
        vending_machine.insert_coin(24.257, 1.956, 5.67)

        vending_machine.process_coins_value()
        assert vending_machine.state == VendingMachineState.CHOOSE_ITEM

        vending_machine.choose_item('candy')
        assert vending_machine.state == VendingMachineState.PUSH_CHANGE

        vending_machine.push_change()
        assert vending_machine.state == VendingMachineState.PUSH_PRODUCT

        vending_machine.push_product()
        assert vending_machine.state == VendingMachineState.SALE_PROCESSED

        vending_machine.reset()
        assert vending_machine.state == VendingMachineState.INSERT_MONEY

    def test_reset(self, vending_machine, stock_items):
        vending_machine.add_items(stock_items)
        vending_machine.insert_coin(17.91, 1.35, 2.268)
        vending_machine.insert_coin(21.21, 1.95, 5)
        vending_machine.insert_coin(24.257, 1.956, 5.67)
        vending_machine.insert_coin(24.257, 1.956, 5.67)

        vending_machine.process_coins_value()
        vending_machine.choose_item('candy')
        vending_machine.push_change()
        vending_machine.push_product()

        vending_machine.reset()
        assert vending_machine.state == VendingMachineState.INSERT_MONEY
        assert vending_machine.item is None
        assert vending_machine.coins == []
        assert vending_machine.invalid_coins == []
        assert vending_machine.money == 0
        assert vending_machine.display_msg == ''
        assert vending_machine.state == VendingMachineState.INSERT_MONEY

    def test_process_order__not_enough_money(self, vending_machine_with_stock, stock_items):
        vending_machine = vending_machine_with_stock
        vending_machine.insert_coin(17.91, 1.35, 2.268)
        vending_machine.insert_coin(24.257, 1.956, 5.67)
        vending_machine.process_coins_value()
        vending_machine.choose_item('candy')
        assert vending_machine.state == VendingMachineState.WARNING_NOT_ENOUGH_MONEY

    @pytest.mark.parametrize('coin_stats, expected', [
        ((17.91, 1.35, 2.268), 0.10),
        ((21.21, 1.95, 5), 0.05),
        ((24.257, 1.956, 5.67), 0.25),
        ((22, 1.95, 5), 0),
        ((0, 0, 0), 0),
        ])
    def test_insert_a_valid_coin_and_calc_value(self, vending_machine, stock_items, coin_stats, expected):
        vending_machine.insert_coin(*coin_stats)
        vending_machine.process_coins_value()
        result = vending_machine.money
        assert result == expected

    def test_get_coins_value(self, vending_machine):
        coins = [
            (17.91, 1.35, 2.268),
            (21.21, 1.95, 5),
            (24.257, 1.956, 5.67),
            (21.21, 1.95, 5),
            (22, 1.95, 5),
            (20, 1.85, 5),
            ]
        for coin in coins:
            vending_machine.insert_coin(*coin)
        vending_machine.process_coins_value()
        result = vending_machine.money
        expected = 0.45
        assert result == expected

    def test_insert_not_valid_coins(self, vending_machine):
        coins = [
            (15.91, 1.35, 2.268),
            (24.257, 1.956, 5.67),
            (22, 5, 3),
            (22, 1.95, 5),
            (0, 0, 0),
            ]
        for coin in coins:
            vending_machine.insert_coin(*coin)
        result = vending_machine.invalid_coins
        expected = [Coin(15.91, 1.35, 2.268),
                    Coin(22, 5, 3),
                    Coin(22, 1.95, 5),
                    Coin(0, 0, 0),
                    ]
        assert repr(result) == repr(expected)
