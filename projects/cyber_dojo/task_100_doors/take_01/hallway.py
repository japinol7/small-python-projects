OPEN_DOOR = True
CLOSED_DOOR = False


class Hallway:
    """Represents a hallway of doors.
    Open doors will be represented by True; closed doors, by False.
    """
    def __init__(self, num_doors):
        self.num_doors = num_doors
        self.doors = [CLOSED_DOOR for _ in range(num_doors)]

    def is_door_open(self, door):
        return self.doors[door]

    def toggle_door(self, door):
        self.doors[door] = not self.doors[door]

    def get_open_doors(self):
        return (door for door, state in enumerate(self.doors, start=1) if state)

    def traverse(self, steps=1):
        for door in range(steps - 1, self.num_doors, steps):
            self.toggle_door(door)

    def traverse_num_doors_times(self):
        """Pass num_doors times by the doors.
        The first time we visit all the doors.
        The second time we only visit every second door.
        The third time, every third door, etc
        """
        for steps in range(1, self.num_doors + 1):
            self.traverse(steps)
