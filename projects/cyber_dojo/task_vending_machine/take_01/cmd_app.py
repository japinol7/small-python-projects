# TODO: WIP. This kata is in development.

from vending_machine_controller import VendingMachineController
from display import Display


class CmdApp:
    def __init__(self):
        self.display = Display()
        self.v_machine = VendingMachineController(display=self.display)

    def run(self):
        self.handle_start()

    def handle_start(self):
        while True:
            print("\n············· JAP Vending Machine ···············" 
                  "\nChoose an option"
                  "\n\t1. Insert coin."
                  "\n\t2. Choose product."
                  "\n\t3. Dispense coins. Cancel order."
                  "\n\t0. Exit program."
                  "\n·········-·······································"
                  "\nState"
                  f"\n\tMoney: {self.v_machine.money}"
                  f"\n\titem: {self.v_machine.item}"
                  f"\n\tDisplay: {self.display.msg}"
                  "\n·········-·······································")
            option = input("Option ? ")
            if '1' in option:
                self.handle_coin_input()
            elif '0' in option:
                exit()

    def handle_coin_input(self):
        while True:
            print("\n············· Insert coins ···············"
                  "\nChoose an option"
                  "\n\t1. Insert Nickel."
                  "\n\t2. Insert Dime."
                  "\n\t3. Insert Quarter."
                  "\n\t0. Return to Start menu."
                  "\n·········-·······································"
                  f"\nDisplay: {self.display.msg}"
                  "\n·········-·······································")
            option = input("Option ? ")
            if '1' in option:
                self.handle_coin_input()
            elif '0' in option:
                self.handle_start()
