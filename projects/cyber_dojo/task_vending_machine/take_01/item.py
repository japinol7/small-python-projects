
class ItemException(Exception):
    pass


class Item:
    def __init__(self, name, price, stock):
        self.name = name
        self.price = price
        self.stock = stock

    @property
    def stock(self):
        return self._stock

    @stock.setter
    def stock(self, value):
        if value < 0:
            raise ItemException("Warning. Stock cannot be a negative value!")
        self._stock = value

    def decrease_stock(self):
        try:
            self.stock -= 1
        except ItemException:
            raise ItemException("This item is sold out!! You cannot decrease 1 unit.")

    def __str__(self):
        return f"name: {self.name}, price: {self.price}, stock: {self.stock}"

    def __repr__(self):
        return f"{self.__class__.__name__}("\
               f"name='{self.name}', price={self.price}, stock={self.stock})"
