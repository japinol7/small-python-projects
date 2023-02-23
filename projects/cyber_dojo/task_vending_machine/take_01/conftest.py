import pytest

from display import Display
from vending_machine import VendingMachine
from vending_machine_controller import VendingMachineController


@pytest.fixture()
def stock_items():
    return [
        {'name': 'candy', 'qty': 4, 'price': 0.65},
        {'name': 'chips', 'qty': 1, 'price': 0.5},
        {'name': 'cola', 'qty': 2, 'price': 1},
        ]


@pytest.fixture()
def vending_machine():
    return VendingMachine(Display())


@pytest.fixture()
def vending_machine_with_stock(stock_items):
    vending_machine = VendingMachine(Display())
    vending_machine.add_items(stock_items)
    return vending_machine


@pytest.fixture()
def v_machine_controller():
    return VendingMachineController(Display())


@pytest.fixture()
def v_machine_controller_with_stock(stock_items):
    v_machine_controller = VendingMachineController(Display())
    v_machine_controller.add_items(stock_items)
    return v_machine_controller
