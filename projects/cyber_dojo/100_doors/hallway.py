class Hallway:
    def __init__(self, num_doors):
        self.num_doors = num_doors
        self.doors = [False for _ in range(num_doors)]

    def is_door_open(self, door):
        return self.doors[door]

    def open_door(self, door):
        self.doors[door] = True

    def close_door(self, door):
        self.doors[door] = False

    def toggle_door(self, door):
        self.doors[door] = not self.doors[door]

    def traverse(self, steps=1):
        for door in range(steps - 1, self.num_doors, steps):
            self.toggle_door(door)

    def traverse_num_doors_times(self):
        """Pass num_doors times by the doors.
        The first time we visit all the doors.
        The second time we only visit every second door.
        The third time, every third door, etc
        """
        for step in range(1, self.num_doors + 1):
            self.traverse(step)

    def get_open_doors(self):
        return [door + 1 for door, state in enumerate(self.doors) if state]


if __name__ == '__main__':
    hallway = Hallway(num_doors=100)
    hallway.traverse_num_doors_times()
    print(f"Open doors: {hallway.get_open_doors()}")
