# TODO: WIP. This kata is in development.

from coin import COIN_STATS, CoinType, COIN_NAMES
from config import CURRENCY_CODE
from vending_machine_controller import VendingMachineController, VendingMachineState, DISPLAY_MSG_STATES
from display import Display

SEPARATOR_LINE = "\n·········-·······································"


class CmdApp:
    def __init__(self):
        self.display = Display()
        self.v_machine = VendingMachineController(display=self.display)

    def run(self):
        self.v_machine.load_items_from_json()
        self.handle_start()

    def handle_start(self):
        while True:
            print("\n············· JAP Vending Machine ···············" 
                  "\nChoose an option"
                  "\n\t1. Insert coin."
                  "\n\t2. Choose product."
                  "\n\t3. Dispense coins. Cancel order."
                  "\n\t0. Exit program."
                  f"{self._get_state_to_print()}"
                  f"{SEPARATOR_LINE}")
            option = input("Option ? ")
            if '0' in option:
                exit()
            elif '1' in option:
                self.handle_coin_input()
            elif '2' in option:
                self.handle_product_input()
            elif '3' in option:
                self.handle_cancel_order()

    def handle_coin_input(self):
        while True:
            print("\n·················· Insert coins ·················"
                  "\nChoose an option"
                  "\n\t1. Insert Nickel."
                  "\n\t2. Insert Dime."
                  "\n\t3. Insert Quarter."
                  "\n\t0. Return to Start menu."
                  f"{self._get_state_to_print()}"
                  f"{SEPARATOR_LINE}")
            option = input("Option ? ")
            if '0' in option:
                self.handle_start()
            elif '1' in option:
                self.v_machine.insert_coin(*COIN_STATS[CoinType.NICKEL])
                self.v_machine.process_coins_value()
            elif '2' in option:
                self.v_machine.insert_coin(*COIN_STATS[CoinType.DIME])
                self.v_machine.process_coins_value()
            elif '3' in option:
                self.v_machine.insert_coin(*COIN_STATS[CoinType.QUARTER])
                self.v_machine.process_coins_value()

    def handle_product_input(self):
        while True:
            products = self.v_machine.get_items_with_numeric_key(start=1)
            print("\n················ Choose product ·················"
                  "\nChoose an option"
                  f"\n\t{self._get_products_to_print(products)}"
                  "\n\t0. Return to Start menu."
                  f"{self._get_state_to_print()}"
                  f"{SEPARATOR_LINE}")
            option = input("Option ? ")
            if '0' in option:
                self.handle_start()
            elif option.isnumeric() and int(option) and int(option) in products:
                self.v_machine.choose_item(products[int(option)].name)
                self.handle_dispense_product()

    def handle_dispense_product(self):
        display_msg = ''
        take_stuff_str = ''
        if self.v_machine.state == VendingMachineState.DISPENSE_CHANGE:
            cash_change = self.v_machine.dispense_change()
            take_stuff_str += "\nRetrieve your change:" \
                              f"\n\t{cash_change} {CURRENCY_CODE}"
        if self.v_machine.state == VendingMachineState.DISPENSE_ITEM:
            take_stuff_str += "\nRetrieve your Product"
            self.v_machine.dispense_item()
            display_msg = DISPLAY_MSG_STATES[self.v_machine.state]
            self.v_machine.reset()

        print("\n··-············ Dispense Product ················"
              f"{take_stuff_str}"
              f"{self._get_state_to_print(display_msg=display_msg)}"
              f"{SEPARATOR_LINE}")
        _ = input("Press enter to return to Start menu ")
        self.handle_start()

    def handle_cancel_order(self):
        coins = self.v_machine.cancel()
        print("\n··-············· Cancel order ···················"
              "\nRetrieve coins ->"
              f"\n\t{self._get_coins_to_print(coins)}"
              f"{self._get_state_to_print()}"
              f"{SEPARATOR_LINE}")
        _ = input("Press enter to return to Start menu ")

    def _get_state_to_print(self, display_msg=None):
        return (f"{SEPARATOR_LINE}"
                "\nState"
                f"\n\tMoney: {self.v_machine.money}"
                f"\n\titem: {self.v_machine.item}"
                f"{SEPARATOR_LINE}"
                "\nDisplay"
                f"\n\tDisplay: {display_msg or self.display.msg}")

    @staticmethod
    def _get_products_to_print(products):
        res = (f'{k:2}. {v.name:.<20} st:{v.stock: 2} | {v.price:5.2f} {CURRENCY_CODE}' for k, v in products.items())
        return '\n\t'.join(res)

    @staticmethod
    def _get_coins_to_print(coins):
        return '\n\t'.join(([COIN_NAMES[x.type] for x in coins]))
