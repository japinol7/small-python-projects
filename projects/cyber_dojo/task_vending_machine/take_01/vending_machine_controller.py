from vending_machine import VendingMachine


class VendingMachineController:
    def __init__(self):
        self.v_machine = VendingMachine()

    def add_items(self, items):
        self.v_machine.add_items(items)

    def process_order(self, item, coins_stats):
        item_sold = True
        for coin_stats in coins_stats:
            self.v_machine.insert_coin(*coin_stats)
        self.v_machine.process_coins_value()

        self.v_machine.choose_item(item)

        self.v_machine.push_product()

        change = self.v_machine.push_change()
        self.v_machine.reset()
        return item_sold, change
