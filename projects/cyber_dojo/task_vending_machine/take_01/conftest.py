import pytest

from display import Display
from coin import CoinType, Coin
from coin_dispenser import CoinDispenser
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
def stock_dispenser_coins():
    coins_types = [CoinType.QUARTER, CoinType.QUARTER, CoinType.QUARTER,
                   CoinType.QUARTER,
                   CoinType.DIME, CoinType.DIME, CoinType.DIME,
                   CoinType.DIME, CoinType.DIME,
                   CoinType.NICKEL, CoinType.NICKEL, CoinType.NICKEL]
    return [Coin(*Coin.get_coin_stats(coin_type))
            for coin_type in coins_types]


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


@pytest.fixture()
def coin_dispenser_with_coins(stock_dispenser_coins):
    return CoinDispenser(stock_dispenser_coins)
