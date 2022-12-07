from itertools import chain, combinations, groupby

HARRY_POTTER_BOOK_PRICE = 8
DISCOUNTS = {
    2: 0.05,
    3: 0.1,
    4: 0.2,
    5: 0.25,
    }
DECIMAL_PRECISION = 2


def powerset(iterable, min_items=0, max_items=None):
    """Examples:
    powerset([1, 2, 3]) --> [(), (1,), (2,), (3,), (1, 2), (1, 3), (2, 3), (1, 2, 3)]
    powerset([1, 2, 3], min_items=2, max_items=2) --> [(1, 2), (1, 3), (2, 3)]
    """
    s = list(iterable)
    if not max_items or max_items > len(s):
        max_items = len(s)
    if min_items < 0:
        min_items = 0
    return chain.from_iterable(combinations(s, r) for r in range(min_items, max_items + 1))


def get_groups_of_different_len(items):
    res = []
    for k, g in groupby(sorted(items, key=lambda x: len(x)), key=lambda x: len(x)):
        res.append(next(g))
    return res


class Item:
    def __init__(self, name, qty):
        self.name = name
        self.qty = qty

    def __repr__(self):
        return f"{self.__class__.__name__}(" \
               f"{self.name}, {self.qty})"


class ShoppingBasket:
    """Represents a shopping basket with only Harry Potter books.
    Each book can only appear once in the shopping basket.
    """
    def __init__(self, items):
        self.items = items

    @staticmethod
    def _get_different_books(items, item_quantities):
        return list({item for item in items if item_quantities[item.name] > 0})

    def _calculate_discount(self, items, item_quantities):
        price_discount = 0
        different_books = self._get_different_books(items, item_quantities)
        different_book_count = len(different_books)
        if different_book_count < 2:
            return price_discount

        price_to_apply_discount = different_book_count * HARRY_POTTER_BOOK_PRICE
        discount = DISCOUNTS.get(different_book_count, 0)
        price_discount += price_to_apply_discount * discount
        for item in different_books:
            item_quantities[item.name] -= 1
        return price_discount

    def get_price(self):
        total_books = sum(item.qty for item in self.items)
        price = total_books * HARRY_POTTER_BOOK_PRICE

        price_discounts = []
        groupings = powerset(self.items, min(DISCOUNTS), max(DISCOUNTS))
        groupings = get_groups_of_different_len(groupings)
        for items in groupings:
            # Calculate discount for the current grouping
            item_quantities = {item.name: item.qty for item in items}
            discount = self._calculate_discount(items, item_quantities)
            # Calculate discount for the rest of the items whether they are in this grouping or not
            item_quantities_total = {item.name: item.qty for item in self.items}
            for key, value in item_quantities.items():
                item_quantities_total[key] = value
            while True:
                discount_rest = self._calculate_discount(self.items, item_quantities_total)
                if discount_rest <= 0:
                    break
                discount += discount_rest
            # Put the discount for this grouping in the possible discounts,
            # so later we can choose the greater discount
            if discount > 0:
                price_discounts += [discount]

        if price_discounts:
            price -= max(price_discounts)
        return round(price, DECIMAL_PRECISION)
