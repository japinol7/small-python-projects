from enum import Enum

from coin import Coin

DECIMALS = 2


class VendingMachineState(Enum):
    CHOOSE_ITEM = 1
    INSERT_MONEY = 2
    PUSH_CHANGE = 3
    PUSH_PRODUCT = 4
    SALE_PROCESSED = 5
    WARNING_SOLD_OUT = 6
    WARNING_NOT_ENOUGH_MONEY = 7
    WARNING_EXACT_CHANGE = 8


DISPLAY_MSG_STATES = {
    VendingMachineState.INSERT_MONEY: 'INSERT COIN',
    VendingMachineState.CHOOSE_ITEM: 'CHOOSE PRODUCT',
    VendingMachineState.PUSH_CHANGE: 'COLLECT YOUR CHANGE',
    VendingMachineState.PUSH_PRODUCT: 'COLLECT YOUR ITEM',
    VendingMachineState.SALE_PROCESSED: 'THANK YOU',
    VendingMachineState.WARNING_SOLD_OUT: 'SOLD OUT',
    VendingMachineState.WARNING_NOT_ENOUGH_MONEY: 'INSERT COIN',
    VendingMachineState.WARNING_EXACT_CHANGE: 'EXACT CHANGE ONLY',
    }


class VendingMachine:
    def __init__(self):
        self._items = {}
        self.item = None
        self.coins = []
        self.invalid_coins = []
        self.money = 0
        self.display_msg = ''
        self._state = VendingMachineState.INSERT_MONEY

    @property
    def items(self):
        return self._items

    @property
    def state(self):
        return self._state

    @state.setter
    def state(self, value):
        self._state = value
        self.display_msg = DISPLAY_MSG_STATES[self.state]

    def reset(self):
        self.item = None
        self.display_msg = ''
        self._state = VendingMachineState.INSERT_MONEY
        self.clean_money()

    def add_items(self, items):
        new_items = {item['name']: item for item in items if not self.items.get(item['name'])}
        new_items.update({
            item['name']: {
                'name': item['name'],
                'price': item['price'],
                'qty': self.items.get(item['name'])['qty'] + item['qty'],
                }
            for item in items if self.items.get(item['name'])
            })
        self.items.update(new_items)

    def remove_item(self, item, qty):
        self.items[item]['qty'] -= qty

    def get_item_price(self, item):
        return self.items[item]['price']

    def get_item_qty(self, item):
        if self.items[item]['qty'] < 1:
            return 'SOLD OUT'
        return self.items[item]['qty']

    def choose_item(self, item):
        if self.get_item_price(item) > self.money:
            self.item = item
            self.state = VendingMachineState.WARNING_NOT_ENOUGH_MONEY
        elif self.get_item_qty(item) != 'SOLD OUT':
            self.item = item
            self.state = VendingMachineState.PUSH_CHANGE

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

    def push_change(self):
        cash_change = round(self.money - self.get_item_price(self.item), DECIMALS)
        self.state = VendingMachineState.PUSH_PRODUCT
        return cash_change

    def clean_money(self):
        self.money = 0
        self.coins = []
        self.invalid_coins = []

    def push_product(self):
        self.remove_item(self.item, 1)
        self.state = VendingMachineState.SALE_PROCESSED
