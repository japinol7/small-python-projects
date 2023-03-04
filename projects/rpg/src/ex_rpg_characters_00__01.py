class Actor:
    def __init__(self, name, type_, health, hit_power, magic_power):
        self.name = name
        self.health = health
        self.hit_power = hit_power
        self.magic_power = magic_power
        self.type_ = type_

    def __str__(self):
        return (f"name: {self.name} \n"
                f"type: {self.type_} \n"
                f"health: {self.health}\n"
                f"hit_power: {self.hit_power}\n"
                f"magic_power: {self.magic_power}")

    def shoot_arrow(self):
        print(f"{self.name} shoots an arrow")


def main():
    baragorn = Actor("Baragorn", "rider", health=100, hit_power=50, magic_power=0)
    player1 = Actor("Player1", "mage", health=65, hit_power=7, magic_power=40)

    print(baragorn)
    print()
    print(player1)

    print()
    baragorn.shoot_arrow()


if __name__ == '__main__':
    main()
