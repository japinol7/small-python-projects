# WIP. Work in progress


class VendingMachine:
    def __init__(self):
        self._items = {}

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

    def remove_item(self, product, qty):
        self.items[product]['qty'] -= qty

    def get_item_price(self, product):
        return self.items[product]['price']

    def get_item_qty(self, product):
        if self.items[product]['qty'] < 1:
            return 'SOLD OUT'
        return self.items[product]['qty']

    def process_order(self, product, input_cash):
        product_sold = True
        cash_change = input_cash - self.get_item_price(product)
        self.remove_item(product, 1)
        return product_sold, cash_change
