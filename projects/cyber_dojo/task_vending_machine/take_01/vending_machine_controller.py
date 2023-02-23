from vending_machine import VendingMachine


class VendingMachineControllerException(Exception):
    pass


class VendingMachineController:
    def __init__(self, display):
        self.v_machine = VendingMachine(display)

    def reset(self):
        self.v_machine.reset()

    def add_items(self, items):
        self.validate_items(items)
        self.v_machine.add_items(items)

    @staticmethod
    def validate_items(items):
        if not items:
            raise VendingMachineControllerException("Warning. You must set some items to add.")

        for item in items:
            if any((not item.get('name'),
                    item.get('price', -1) < 0,
                    item.get('qty', -1) < 0
                    )):
                raise VendingMachineControllerException(
                    f"Warning. Item have an invalid name, price or qty field: {item}")

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

    def cancel(self):
        return self.v_machine.push_coins()

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
