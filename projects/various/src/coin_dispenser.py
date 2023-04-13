DECIMALS = 2


class CoinDispenserNotEnoughPaymentException(Exception):
    pass


class CoinDispenserCannotProvideExactChangeException(Exception):
    pass


class CoinDispenser:
    def __init__(self, coins: list[float]):
        self.coins = coins

    def get_change_coins(self, cost: float, payment: float) -> list[float]:
        """Returns the coins to be returned as change"""
        if payment < cost:
            raise CoinDispenserNotEnoughPaymentException(
                "Payment is less than the cost")

        change_amount = round(payment - cost, DECIMALS)
        change_coins = []
        for coin in sorted(self.coins, reverse=True):
            while change_amount >= coin:
                change_coins += [coin]
                change_amount -= coin

        if change_amount:
            raise CoinDispenserCannotProvideExactChangeException(
                "Cannot provide exact change with the available coins")

        return change_coins


def _test_coin_dispenser():
    coins = [0.25, 0.25, 0.25, 0.25,
             0.10, 0.10, 0.10, 0.10, 0.10,
             0.05, 0.05, 0.05]
    cost = 1.3
    payment = 1.50
    coin_dispenser = CoinDispenser(coins)
    result = coin_dispenser.get_change_coins(cost, payment)
    expected = [0.10, 0.10]
    print("Calculate change coins given these inputs:\n"
          f"\tCoins in the machine: {coins}\n"
          f"\t\t\tTotal coins in the machine value: {round(sum(coins), DECIMALS)}\n"
          f"\tCost of the product: {cost}\n"
          f"\tPayment: {payment}\n"
          f"Result:\n"
          f"\t{result}\n"
          f"Expected:\n"
          f"\t{expected}\n\n"
          f"Test {'OK' if result == expected else 'FAILED'}"
          )


if __name__ == '__main__':
    _test_coin_dispenser()
