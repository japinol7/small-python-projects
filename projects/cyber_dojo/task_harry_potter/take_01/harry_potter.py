HARRY_POTTER_BOOK_PRICE = 8
DISCOUNTS = {
    2: 0.05,
    3: 0.1,
    4: 0.2,
    5: 0.25,
    }


class Item:
    def __init__(self, name, qty):
        self.name = name
        self.qty = qty


class ShoppingBasket:
    """Represents a shopping basket with only Harry Potter books.
    Each book can only appear once in the shopping basket.
    """
    def __init__(self, items):
        self.items = items
        self.item_quantities = {item.name: item.qty for item in items}
        self.max_item_qty = max(item.qty for item in self.items) if self.items else 0

    def _get_different_books(self):
        return [item for item in self.items if self.item_quantities[item.name] > 0]

    def _calculate_discount(self):
        price_discount = 0
        while True:
            different_books = self._get_different_books()
            different_book_count = len(different_books)
            if different_book_count < 2:
                break
            price_to_apply_discount = different_book_count * HARRY_POTTER_BOOK_PRICE
            discount = DISCOUNTS.get(different_book_count, 0)
            price_discount += price_to_apply_discount * discount
            for item in self._get_different_books():
                self.item_quantities[item.name] -= 1
        return price_discount

    def get_price(self):
        total_books = sum(item.qty for item in self.items)
        price = total_books * HARRY_POTTER_BOOK_PRICE

        price_discount = self._calculate_discount()
        price -= price_discount
        return price
