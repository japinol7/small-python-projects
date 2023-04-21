import pytest

from vending_machine_controller import VendingMachineControllerException, VendingMachineState
from coin import Coin, CoinType


class TestVendingMachine:

    @pytest.mark.parametrize('items', [
        [{'name': 'chips', 'price': 0.5}],
        [{'name': 'cola', 'qty': 2, 'price': -1}],
        [{'name': 'chips', 'qty': 1, 'price': 0.5},
         {'n': 'cola', 'qty': 2, 'price': 1}],
        [{}],
        None,
        ])
    def test_add_items_with_invalid_fields_must_raise_exception(self, items, v_machine_controller):
        with pytest.raises(VendingMachineControllerException):
            v_machine_controller.add_items(items)

    def test_cancel_after_insert_some_money(self, v_machine_controller):
        coins = [
            (17.91, 1.35, 2.268),
            (21.21, 1.95, 5),
            (24.257, 1.956, 5.67),
            (21.21, 1.95, 5),
            ]
        for coin in coins:
            v_machine_controller.insert_coin(*coin)
        result = v_machine_controller.cancel()
        expected = "[Coin(17.91, 1.35, 2.268), " \
                   "Coin(21.21, 1.95, 5), " \
                   "Coin(24.257, 1.956, 5.67), " \
                   "Coin(21.21, 1.95, 5)]"
        assert repr(result) == expected

    @pytest.mark.parametrize('coin_stats, expected', [
        ((24.257, 1.956, 5.67), 0.25),
        ((17.91, 1.35, 2.268), 0.10),
        ((24.257, 1.15, 5), 0),
        ((0, 0, 0), 0),
        ])
    def test_insert_a_valid_coin_and_calc_value(self, v_machine_controller, stock_items, coin_stats, expected):
        v_machine_controller.insert_coin(*coin_stats)
        v_machine_controller.process_coins_value()
        result = v_machine_controller.money
        assert result == expected

    def test_insert_not_valid_coins(self, v_machine_controller):
        coins = [
            (22, 5, 3),
            (24.257, 1.956, 5.67),
            (15.91, 1.35, 2.268),
            (0, 0, 0),
            ]
        for coin in coins:
            v_machine_controller.insert_coin(*coin)
        result = v_machine_controller.invalid_coins
        expected = [Coin(22, 5, 3),
                    Coin(15.91, 1.35, 2.268),
                    Coin(0, 0, 0),
                    ]
        assert repr(result) == repr(expected)

    @pytest.mark.parametrize('item, coins, expected', [
        ('chips',
            [(24.257, 1.956, 5.67),
             (24.257, 1.956, 5.67),
             (24.257, 1.956, 5.67),
             (24.257, 1.956, 5.67),
             ],
            (True, (0.5, [Coin(24.257, 1.956, 5.67), Coin(24.257, 1.956, 5.67)]))
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
            (True, (0.85, [
                Coin(24.257, 1.956, 5.67), Coin(24.257, 1.956, 5.67),
                Coin(24.257, 1.956, 5.67), Coin(17.91, 1.35, 2.268)
                ]))
         ),
        ])
    def test_process_order(self, v_machine_controller_with_stock_and_coins_to_dispense,
                           stock_items, item, coins, expected):
        result = v_machine_controller_with_stock_and_coins_to_dispense.process_order(item, coins)
        assert str(result) == str(expected)

    def test_get_items_with_numeric_key(self, v_machine_controller_with_stock):
        v_machine = v_machine_controller_with_stock
        v_machine.insert_coin(24.257, 1.956, 5.67)
        v_machine.insert_coin(24.257, 1.956, 5.67)
        v_machine.choose_item('chips')
        v_machine.reset()
        result = v_machine.get_items_with_numeric_key(start=1)
        expected = ("{1: Item(name='candy', price=0.65, stock=4), "
                    "2: Item(name='chips', price=0.5, stock=1), "
                    "3: Item(name='cola', price=1, stock=2)}")
        assert str(result) == expected

    def test_get_items_with_stock(self, v_machine_controller_with_stock):
        v_machine = v_machine_controller_with_stock
        v_machine.insert_coin(24.257, 1.956, 5.67)
        v_machine.insert_coin(24.257, 1.956, 5.67)
        v_machine.process_coins_value()
        v_machine.choose_item('chips')
        v_machine.dispense_item()
        v_machine.reset()
        result = v_machine.get_items_with_stock()
        expected = ("{'candy': Item(name='candy', price=0.65, stock=4), "
                    "'cola': Item(name='cola', price=1, stock=2)}")
        assert str(result) == expected

    def test_get_items_with_stock_with_numeric_key(self, v_machine_controller_with_stock):
        v_machine = v_machine_controller_with_stock
        v_machine.insert_coin(24.257, 1.956, 5.67)
        v_machine.insert_coin(24.257, 1.956, 5.67)
        v_machine.process_coins_value()
        v_machine.choose_item('chips')
        v_machine.dispense_item()
        v_machine.reset()
        result = v_machine.get_items_with_stock_with_numeric_key(start=1)
        expected = ("{1: Item(name='candy', price=0.65, stock=4), "
                    "3: Item(name='cola', price=1, stock=2)}")
        assert str(result) == expected

    @pytest.mark.parametrize('diameter, thickness, weight, expected', [
        (21.21, 1.95, 5, CoinType.NICKEL),
        (17.91, 1.35, 2.268, CoinType.DIME),
        (24.257, 1.956, 5.67, CoinType.QUARTER),
        (23, 2, 5, CoinType.NONE),
        (0, 0, 0, CoinType.NONE),
        ])
    def test_get_coin_type(self, diameter, thickness, weight, expected):
        result = Coin(diameter, thickness, weight).type
        assert result == expected

    @pytest.mark.parametrize('item, expected', [
        (('chips', []), 0),
        (('candy', []), 3),
        ])
    def test_after_process_order_stock_will_be_updated(self, v_machine_controller_with_stock, stock_items, item, expected):
        v_machine_controller_with_stock.process_order(*item)
        result = v_machine_controller_with_stock.v_machine.get_item_qty(item[0])
        assert result == expected

    def test_process_order__not_enough_stock(self, v_machine_controller_with_stock, stock_items):
        items_coins_n_expected = [
            ({'item_name': 'cola',
              'coins_stats': [(24.257, 1.956, 5.67), (24.257, 1.956, 5.67)]},
             VendingMachineState.DISPENSE_ITEM),
            ({'item_name': 'cola',
              'coins_stats': [(24.257, 1.956, 5.67), (24.257, 1.956, 5.67)]},
             VendingMachineState.DISPENSE_ITEM),
            ({'item_name': 'cola',
              'coins_stats': [(24.257, 1.956, 5.67), (24.257, 1.956, 5.67)]},
             VendingMachineState.WARNING_SOLD_OUT),
            ]

        for values, expected in items_coins_n_expected:
            v_machine_controller_with_stock.process_order(**values)
            result = v_machine_controller_with_stock.state
            assert result == expected

    def test_process_order_reset(self, v_machine_controller_with_stock, stock_items):
        items_n_coins = [
            {'item_name': 'cola',
             'coins_stats': [(24.257, 1.956, 5.67), (24.257, 1.956, 5.67)]},
            {'item_name': 'cola',
             'coins_stats': [(24.257, 1.956, 5.67), (24.257, 1.956, 5.67)]},
            ]

        for item_n_coin in items_n_coins:
            v_machine_controller_with_stock.process_order(**item_n_coin)
            v_machine_controller_with_stock.reset()
            assert v_machine_controller_with_stock.state == VendingMachineState.INSERT_MONEY
            assert v_machine_controller_with_stock.item is None
            assert v_machine_controller_with_stock.coins == []
            assert v_machine_controller_with_stock.invalid_coins == []
            assert v_machine_controller_with_stock.money == 0
