import math


class Hallway:
    def __init__(self, num_doors):
        self.num_doors = num_doors

    def get_doors_to_open(self):
        """Gets doors to open if we traverse the hallway this way:
        Pass num_doors times by the doors.
        The first time we visit all the doors.
        The second time we only visit every second door.
        The third time, every third door, etc
        We know from the first try with program take_01 that
        the solution for an input of 100 doors is this list of doors open:
        [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
        Now we can easily see a pattern, and take advantage of it.
        The open doors are the squares of the consecutive integers from 1 to sqrt(num_doors).
        """
        return (door * door for door in range(1, int(math.sqrt(self.num_doors) + 1)))
