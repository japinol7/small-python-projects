from pprint import pprint
from abc import ABCMeta, abstractmethod


class ActorExistsException(Exception):
    pass


class Actor(metaclass=ABCMeta):
    actors = {}

    def __init__(self, name, type, health, power):
        if name in self.__class__.actors:
            raise ActorExistsException
        self.type_actor = None
        self.name = name
        self.__class__.actors[name] = self
        self.type = type
        self.health = health
        self.power = power

    def __str__(self):
        return (f"name: {self.name!r}, "
                f"type: {self.type!r}, "
                f"health: {self.health!r}, "
                f"power: {self.power!r}")

    def  __repr__(self):
        return (f"{self.type_actor}("
                f"{self.name!r}, "
                f"{self.type!r}, "
                f"{self.health!r}, "
                f"{self.power!r})")
               
    @abstractmethod
    def greet(self):
        pass


class Npc(Actor):
    npcs = {}

    def __init__(self, name, type, health, power):
        super().__init__(name, type, health, power)
        self.__class__.npcs[name] = self
        self.type_actor = 'Npc'

    def greet(self):
        print('Hello!')


class Pc(Actor):
    pcs = {}

    def __init__(self, name, type, health, power):
        super().__init__(name, type, health, power)
        self.__class__.pcs[name] = self
        self.type_actor = 'Pc'

    def greet(self):
        print('Hi!')


def main():
    baragorn = Npc("Baragorn", "rider", 100, 20)
    player1 = Pc("Player1", "rider", 50, 20)
    npc_def = [
        ("Aragorn", "rider", 100, 20),
        ("Gandalf", "mage", 110, 520),
    ]

    some_npcs = [Npc(*npc) for npc in npc_def]

    print("Baragon:")
    pprint(baragorn)
    print("\nplayer1:")
    pprint(player1)
    print("\nsome_npcs:")
    pprint(some_npcs)

    print("\nActors:")
    pprint(Actor.actors)
    print("\nNpcs:")
    pprint(Npc.npcs)
    print("\nPcs:")
    pprint(Pc.pcs)


if __name__ == '__main__':
    main()
