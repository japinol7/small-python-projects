from vending_machine import VendingMachine


class VendingMachineController:
    def __init__(self):
        self.v_machine = VendingMachine()

    def reset(self):
        self.v_machine.reset()

    def add_items(self, items):
        self.v_machine.add_items(items)

    def insert_coin(self, diameter, thickness, weight):
        self.v_machine.insert_coin(diameter, thickness, weight)

    def process_coins_value(self):
        self.v_machine.process_coins_value()

    def choose_item(self, item):
        self.v_machine.choose_item(item)

    def push_product(self):
        self.v_machine.push_product()

    def push_change(self):
        return self.v_machine.push_change()

    def process_order(self, item, coins_stats):
        item_sold = True
        for coin_stats in coins_stats:
            self.insert_coin(*coin_stats)
        self.process_coins_value()

        self.choose_item(item)
        self.push_product()
        change = self.push_change()

        self.reset()
        return item_sold, change
