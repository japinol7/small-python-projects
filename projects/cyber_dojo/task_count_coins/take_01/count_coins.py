class CountCoins:
    coins = {'quarters': 1,
             'dimes': 5,
             'nickels': 10,
             'pennies': 25,
             }

    def changes(self, amount):
        if amount < 1:
            return 0

        ways = [0] * (amount + 1)
        ways[0] = 1
        for coin in self.__class__.coins.values():
            for j in range(coin, amount + 1):
                ways[j] += ways[j - coin]
        return ways[amount]
