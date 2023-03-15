from enum import Enum

from coin import Coin
from item import Item

DECIMALS = 2


class VendingMachineState(Enum):
    CHOOSE_ITEM = 1
    INSERT_MONEY = 2
    DISPENSE_CHANGE = 3
    DISPENSE_ITEM = 4
    ORDER_PROCESSED = 5
    ORDER_CANCELLED = 6
    WARNING_SOLD_OUT = 7
    WARNING_NOT_ENOUGH_MONEY = 10
    WARNING_EXACT_CHANGE = 11


DISPLAY_MSG_STATES = {
    VendingMachineState.INSERT_MONEY: 'INSERT COIN',
    VendingMachineState.CHOOSE_ITEM: 'CHOOSE PRODUCT',
    VendingMachineState.DISPENSE_CHANGE: 'COLLECT YOUR CHANGE',
    VendingMachineState.DISPENSE_ITEM: 'COLLECT YOUR ITEM',
    VendingMachineState.ORDER_PROCESSED: 'THANK YOU',
    VendingMachineState.ORDER_CANCELLED: 'ORDER CANCELLED',
    VendingMachineState.WARNING_SOLD_OUT: 'SOLD OUT',
    VendingMachineState.WARNING_NOT_ENOUGH_MONEY: 'INSERT COIN',
    VendingMachineState.WARNING_EXACT_CHANGE: 'EXACT CHANGE ONLY',
    }


class VendingMachine:
    def __init__(self, display):
        self._items = {}
        self.item = None
        self.coins = []
        self.invalid_coins = []
        self.money = 0
        self._state = VendingMachineState.INSERT_MONEY
        self._display = display

    @property
    def items(self):
        return self._items

    @property
    def state(self):
        return self._state

    @state.setter
    def state(self, value):
        self._state = value
        self.display.msg = DISPLAY_MSG_STATES[self.state]

    @property
    def display(self):
        return self._display

    @display.setter
    def display(self, value):
        self._display = value

    def reset(self):
        self.item = None
        self.display.msg = ''
        self._state = VendingMachineState.INSERT_MONEY
        self.clean_money()

    def add_items(self, items):
        """ Adds items to the vending machine.
        Example of input items values:
        [{'name': 'cola', 'qty': 10, 'price': 0.65},]
        """
        new_items = {item['name']: Item(item['name'], item['price'], item['qty'])
                     for item in items if not self.items.get(item['name'])}
        new_items.update({
            item['name']:
                Item(item['name'], item['price'], stock=item['qty'] + self.items.get(item['name'], 0).stock)
            for item in items if self.items.get(item['name'])
            })
        self.items.update(new_items)

    def get_item_price(self, item_name):
        return self.items[item_name].price

    def get_item_qty(self, item_name):
        return self.items[item_name].stock

    def choose_item(self, item_name):
        self.item = self.items[item_name]

        if self.get_item_price(item_name) > self.money:
            self.state = VendingMachineState.WARNING_NOT_ENOUGH_MONEY
            return

        if self.get_item_qty(item_name) < 1:
            self.state = VendingMachineState.WARNING_SOLD_OUT
            return

        self.state = VendingMachineState.DISPENSE_CHANGE

    @staticmethod
    def _is_coin_valid(coin):
        return coin.value > 0

    def insert_coin(self, diameter, thickness, weight):
        coin = Coin(diameter, thickness, weight)
        if not self._is_coin_valid(coin):
            self.invalid_coins += [coin]
            return
        self.coins += [coin]

    def process_coins_value(self):
        self.money = sum(coin.value for coin in self.coins)
        self.state = VendingMachineState.CHOOSE_ITEM

    def dispense_change(self):
        cash_change = round(self.money - self.get_item_price(self.item.name), DECIMALS)
        self.state = VendingMachineState.DISPENSE_ITEM
        return cash_change

    def dispense_coins(self):
        coins = self.coins
        self.reset()
        return coins

    def clean_money(self):
        self.money = 0
        self.coins = []
        self.invalid_coins = []

    def dispense_item(self):
        self.item.decrease_stock()
        self.state = VendingMachineState.ORDER_PROCESSED
