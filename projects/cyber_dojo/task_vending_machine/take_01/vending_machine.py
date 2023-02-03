from enum import Enum


class VendingMachineState(Enum):
    CHOOSE_ITEM = 1
    INSERT_MONEY = 2
    SALE_PROCESSED = 3


class VendingMachine:
    def __init__(self):
        self._items = {}
        self.item = None
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
                 'qty': self.items.get(item['name'])['qty'] + item['qty']
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
        if self.get_item_qty(item) != 'SOLD OUT':
            self.state = VendingMachineState.INSERT_MONEY
            self.item = item

    def insert_money(self, input_cash):
        item_sold = True
        cash_change = input_cash - self.get_item_price(self.item)
        self.remove_item(self.item, 1)
        self.state = VendingMachineState.SALE_PROCESSED
        return item_sold, cash_change

    def process_order(self, item, input_cash):
        self.choose_item(item)
        return self.insert_money(input_cash)
