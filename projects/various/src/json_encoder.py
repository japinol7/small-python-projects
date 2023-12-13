from collections import OrderedDict
from decimal import Decimal
from pprint import pformat
import json


class JsonEncoder:
    """Represents a json encoder that enables the inherit class to be encoded with json dumps.
    The motivation for this class is to allow for json or dict deep representations
    of embedded data structures.
    The generated json only will take into account the instance attributes added in the
    keys class attribute of each subclass.
    Basically, it returns a nice str of the subclasses data structure using str,
    a repr representation of the subclasses data structure using repr,
    and/or a json representation of the subclasses data structure using the method to_json that
    elevates json dumps representation of the to_dict method with simplejson support.
    You can also use the to_dict method for a dict representation of the structure
    without using auto pretty print formatting or the repr functionality.
    To prevent circular refs when an object has a parent object, the parent attribute with name 'parent'
    will be rendered as empty (None) if the parent object does not have an id attribute;
    otherwise, it will be rendered with only the id attribute.
    """
    keys = []

    def __init__(self):
        pass

    @staticmethod
    def _has_to_dict(attr):
        return 'to_dict' in dir(attr) and callable(getattr(attr, 'to_dict'))

    def to_dict(self):
        res = {}
        for key in self.keys:
            val = getattr(self, key)
            if key == 'parent':
                # Prevent circular refs when an object has a parent object and may be also referenced by its parent
                res['parent_id'] = val.id if val and getattr(val, 'id', None) else None
            elif self._has_to_dict(val):
                res[key] = val.to_dict()
            elif type(val) == list:
                res[key] = [self._has_to_dict(v) and v.to_dict() or v for v in val]
            elif type(val) == Decimal:
                res[key] = str(val)
            else:
                res[key] = val

        return OrderedDict(res)

    def __json__(self):
        """Uses json dumps to serialize the to_dict method's result to json."""
        return json.dumps(self.to_dict())

    to_json = __json__

    def __str__(self):
        return pformat(self.to_dict())

    def __repr__(self):
        return repr(self.to_dict())


def main():
    """Example of usage."""
    from decimal import Decimal

    class MenuItem(JsonEncoder):
        keys = ['id', 'name', 'qty', 'price']

        def __init__(self, id_, name, qty, price):
            super(MenuItem, self).__init__()
            self.id = id_
            self.name = name
            self.qty = qty
            self.price = price

    class User(JsonEncoder):
        keys = ['id', 'username', 'name', 'email', 'friends', 'menu_items']

        def __init__(self, id_=None, username=None, name=None, email=None,
                     friends=None, menu_items=None):
            super(User, self).__init__()
            self.id = id_
            self.username = username
            self.name = name
            self.email = email
            self.friends = friends if friends else []
            self.menu_items = menu_items if menu_items else []

    class Data(JsonEncoder):
        keys = ['users']

        def __init__(self, users=None):
            super(Data, self).__init__()
            self.users = users if users else []

    menu_item_1 = MenuItem(100, 'Greek salad', qty=2, price=Decimal('7.5'))
    menu_item_2 = MenuItem(105, 'Pasta Carbonara', qty=1, price=Decimal('8.25'))
    menu_item_3 = MenuItem(107, 'Lemon Dessert', qty=2, price=Decimal('4.5'))
    user_friend_1 = User(7, 'andrea', 'Andrea', 'andrea@andrea.andrea.com',
                         menu_items=[menu_item_2])
    user_friend_2 = User(8, 'geralt', 'Geralt', 'geralt@geralt.geralt.com')

    data = Data([
            User(1, 'j_silver', 'John Silver', 'j_silver@j_silver.j_silver.com'),
            User(5, 'j_pinol', 'Joan Pinol', 'j_pinol@j_pinol.j_pinol.com',
                 friends=[user_friend_1, user_friend_2],
                 menu_items=[menu_item_1, menu_item_3]),
            user_friend_1,
            user_friend_2,
            ]
        )

    print("Data instance representation as str:\n")
    print(data)
    print("\n-----\nData instance representation as repr:\n")
    print(repr(data))
    print("\n-----\nData instance representation as json:\n")
    print(data.to_json())


if __name__ == '__main__':
    main()
