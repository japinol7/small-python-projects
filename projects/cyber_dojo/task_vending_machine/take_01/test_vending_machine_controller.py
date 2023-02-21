import pytest

from vending_machine_controller import VendingMachineControllerException


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
    def test_process_order(self, v_machine_controller_with_stock, stock_items, item, coins, expected):
        result = v_machine_controller_with_stock.process_order(item, coins)
        assert result == expected

    @pytest.mark.parametrize('item, expected', [
        (('chips', []), 'SOLD OUT'),
        (('candy', []), 3),
        ])
    def test_after_process_order_stock_will_be_updated(self, v_machine_controller_with_stock, stock_items, item, expected):
        v_machine_controller_with_stock.process_order(*item)
        result = v_machine_controller_with_stock.v_machine.get_item_qty(item[0])
        assert result == expected

    def test_process_order__not_enough_stock(self, v_machine_controller_with_stock, stock_items):
        items_n_expected = [
            ({'name': 'chips', 'price': []}, 'SOLD OUT'),
            ({'name': 'cola', 'price': []}, 1),
            ({'name': 'cola', 'price': []}, 'SOLD OUT'),
            ]

        for item, expected in items_n_expected:
            v_machine_controller_with_stock.process_order(*item.values())
            result = v_machine_controller_with_stock.v_machine.get_item_qty(item['name'])
            assert result == expected
