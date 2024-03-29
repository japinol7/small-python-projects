import json

from vending_machine import VendingMachine, VendingMachineState, DISPLAY_MSG_STATES
from config import INVENTORY_FILE


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

    def load_items_from_json(self):
        with open(INVENTORY_FILE, 'r') as fin:
            items = json.loads(fin.read())
        self.add_items(items)

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

    @property
    def state(self):
        return self.v_machine.state

    @property
    def money(self):
        return self.v_machine.money

    @property
    def coins(self):
        return self.v_machine.coins

    @property
    def invalid_coins(self):
        return self.v_machine.invalid_coins

    @property
    def item(self):
        return self.v_machine.item

    @property
    def items(self):
        return self.v_machine.items

    def get_items_with_numeric_key(self, start=0):
        return {i: v for i, v in enumerate(self.items.values(), start=start)}

    def get_items_with_stock(self):
        return dict(filter(lambda pair: pair[1].stock > 0, self.items.items()))

    def get_items_with_stock_with_numeric_key(self, start=0):
        return {i: v for i, v in enumerate(self.items.values(), start=start) if v.stock > 0}

    def insert_coin(self, diameter, thickness, weight):
        self.v_machine.insert_coin(diameter, thickness, weight)

    def insert_coin_dispense_change(self, diameter, thickness, weight):
        self.v_machine.insert_coin_dispense_change(diameter, thickness, weight)

    def process_coins_value(self):
        self.v_machine.process_coins_value()

    def choose_item(self, item_name):
        self.v_machine.choose_item(item_name)

    def dispense_item(self):
        self.v_machine.dispense_item()

    def dispense_change(self):
        return self.v_machine.dispense_change()

    def cancel(self):
        return self.v_machine.dispense_coins()

    @staticmethod
    def get_coin_type(coin):
        return coin.get_coin_type(coin)

    def process_order(self, item_name, coins_stats):
        """Intended to be used as a simple way to process an order
        with a unique API call from a remote client, such a microserver.
        """
        item_sold = True
        for coin_stats in coins_stats:
            self.insert_coin(*coin_stats)
        self.process_coins_value()

        self.choose_item(item_name)

        change = 0
        if self.state != VendingMachineState.WARNING_SOLD_OUT:
            self.dispense_item()
            change = self.dispense_change()

        return item_sold, change
