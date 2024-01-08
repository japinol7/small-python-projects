import copy
from abc import ABCMeta, abstractmethod

SECTOR_SEPARATOR = '\n' + '-' * 10


class ActorExistsException(Exception):
    pass


class ItemExistsException(Exception):
    pass


class Actor(metaclass=ABCMeta):
    actors = {}

    def __init__(self, name, type, health, power):
        if name in self.__class__.actors:
            raise ActorExistsException
        self.type_actor = None
        self._name = name
        self.__class__.actors[name] = self
        self.type = type
        self.health = health
        self.power = power
        self.items = []

    def __str__(self):
        return (f"name: {self.name!r}, "
                f"class: {self.type_actor!r}, "
                f"type: {self.type!r}, "
                f"health: {self.health!r}, "
                f"power: {self.power!r}, "
                f"items: {self.items!r}")

    def __repr__(self):
        return (f"{self.type_actor}("
                f"{self.name!r}, "
                f"{self.type!r}, "
                f"{self.health!r}, "
                f"{self.power!r})")

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, v):
        if v in Actor.actors:
            raise ActorExistsException
        Actor.actors[v] = Actor.actors.pop(self._name)
        self._name = v

    def copy(self, v):
        if v in self.actors:
            raise ActorExistsException
        cp = copy.deepcopy(self)
        cp._name = v
        Actor.actors[v] = cp
        return cp

    @abstractmethod
    def greet(self):
        pass


class Npc(Actor):
    npcs = {}

    def __init__(self, name, type, health, power):
        super().__init__(name, type, health, power)
        self.__class__.npcs[name] = self
        self.type_actor = 'Npc'

    @property
    def name(self):
        return super().name

    @name.setter
    def name(self, v):
        if v == self._name:
            return
        old_name = self._name
        super(Npc, self.__class__).name.fset(self, v)
        Npc.npcs[v] = Npc.npcs.pop(old_name)

    def copy(self, v):
        Npc.npcs[v] = super().copy(v)
        return Npc.npcs[v]

    def greet(self):
        print('Hello!')


class Pc(Actor):
    pcs = {}

    def __init__(self, name, type, health, power):
        super().__init__(name, type, health, power)
        self.__class__.pcs[name] = self
        self.type_actor = 'Pc'

    @property
    def name(self):
        return super().name

    @name.setter
    def name(self, v):
        if v == self._name:
            return
        old_name = self._name
        super(Pc, self.__class__).name.fset(self, v)
        Pc.pcs[v] = Pc.pcs.pop(old_name)

    def copy(self, v):
        Pc.pcs[v] = super().copy(v)
        return Pc.pcs[v]

    def greet(self):
        print('Hi!')


class ItemType:
    """ Represents an item type.
    Just for fun, we allow item types with the same name, so we can use dunder methods
    that change the behaviour hos the identity on the items and their hash calculation.
    """
    item_types = {}
    next_id = 1

    def __init__(self, name):
        self.name = name
        self.id = self.__class__.next_id
        self.__class__.item_types[self.id] = self
        self.__class__.next_id += 1

    def __eq__(self, other):
        return self.name == other.name

    def __hash__(self):
        return hash(self.name)

    def __str__(self):
        return (f"id: {self.id!r}, "
                f"name: {self.name!r}")

    def __repr__(self):
        return (f"{self.__class__.__name__}("
                f"{self.name!r})")

    @classmethod
    def get_all_unique_item_types(cls):
        return list(set(cls.item_types.values()))


class Item:
    items = {}

    def __init__(self, name, item_type, health=0):
        if name in self.__class__.items:
            raise ActorExistsException
        self._name = name
        self.item_type = item_type
        self.__class__.items[name] = self
        self.health = health

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, v):
        if v in Item.items:
            raise ItemExistsException
        Item.items[v] = Item.items.pop(self._name)
        self._name = v

    def __str__(self):
        return (f"name: {self.name}, \n"
                f"\thealth: {self.health}, \n"
                f"\titem_type: {self.item_type}"
                )

    def __repr__(self):
        return (f"{self.__class__.__name__}("
                f"{self.name!r}, "
                f"{self.item_type!r}, "
                f"{self.health!r})")


def print_item_types_with_items():
    print(SECTOR_SEPARATOR)
    print("Get all item types")
    for item_type in ItemType.item_types.values():
        print(f'Item type: {item_type}')


def print_actors_with_items():
    print(f"{SECTOR_SEPARATOR} \nActors with items")
    for actor in Actor.actors.values():
        if not actor.items:
            continue
        print(f'Actor: {actor}')


def main():
    # Create some actors
    p1 = Pc("P1", "rider", 50, 20)
    Pc("P2", "rider", 35, 45)
    Pc("P3", "rider", 67, 33)
    baragorn = Npc("Baragorn", "fighter", 100, 20)

    npc_def = [
        ("Aragorn", "rider", 100, 20),
        ("Gandalf", "mage", 110, 520),
        ("Legolas", "thief", 110, 520),
        ]
    [Npc(*npc) for npc in npc_def]

    for actor in Actor.actors.values():
        print(repr(actor))

    default_pc = p1
    default_npc = baragorn
    print(SECTOR_SEPARATOR)
    print(f'Default pc: {default_pc}')
    print(f'Default npc: {default_npc}')

    # Create some item types
    item_type_broadsword = ItemType('broadsword')
    ItemType('longsword')
    item_type_broadsword_2 = ItemType('broadsword')
    print_item_types_with_items()

    # Get the item types without repeated names:
    print(f"{SECTOR_SEPARATOR} \nGet all unique item types, i.e., only one name for item type")
    for item_type in ItemType.get_all_unique_item_types():
        print(f'Item type: {item_type}')

    # Create some items for the actors
    items_def = [
        ('Aeronflight', item_type_broadsword),
        ('Common Broadsword', item_type_broadsword),
        ('Common Broadsword 2', item_type_broadsword_2),
        ]
    [Item(*item) for item in items_def]
    print(SECTOR_SEPARATOR)
    for item in Item.items.values():
        print(f'Item: {item}')

    # Assign some items to actors
    baragorn.items.append(Item.items['Common Broadsword'])
    Actor.actors['P1'].items.append(Item.items['Aeronflight'])
    print_actors_with_items()


if __name__ == '__main__':
    main()
