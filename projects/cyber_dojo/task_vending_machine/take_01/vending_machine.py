from enum import Enum

from coin import Coin

DECIMALS = 2


class VendingMachineState(Enum):
    CHOOSE_ITEM = 1
    INSERT_MONEY = 2
    PUSH_CHANGE = 3
    SALE_NOT_ENOUGH_MONEY = 4
    PUSH_PRODUCT = 5
    SALE_PROCESSED = 6


class VendingMachine:
    def __init__(self):
        self._items = {}
        self.item = None
        self.coins = []
        self.money = 0
        self.state = VendingMachineState.CHOOSE_ITEM

    @property
    def items(self):
        return self._items

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

    def _set_state(self, state):
        self.state = state

    def choose_item(self, item):
        if self.get_item_qty(item) != 'SOLD OUT':
            self._set_state(VendingMachineState.INSERT_MONEY)
            self.item = item

    def insert_coin(self, diameter, thickness, weight):
        coin = Coin(diameter, thickness, weight)
        self.coins += [coin]

    def process_coins_value(self):
        self.money = sum(coin.value for coin in self.coins)
        self._set_state(VendingMachineState.PUSH_CHANGE)

    def push_change(self):
        cash_change = round(self.money - self.get_item_price(self.item), DECIMALS)
        self._set_state(VendingMachineState.PUSH_PRODUCT)
        return cash_change

    def clean_money(self):
        self.money = 0
        self.coins = []

    def push_product(self):
        self.remove_item(self.item, 1)
        self._set_state(VendingMachineState.SALE_PROCESSED)

    def process_order(self, item, coins_stats):
        item_sold = True
        self.choose_item(item)

        for coin_stats in coins_stats:
            self.insert_coin(*coin_stats)
        self.process_coins_value()

        self.push_product()

        change = self.push_change()
        self.clean_money()
        return item_sold, change
