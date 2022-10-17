from hallway import Hallway, OPEN_DOOR, CLOSED_DOOR

ARBITRARY_SMALL_NUM_DOORS = 2
ARBITRARY_NUM_DOORS = 4


class TestHallway:
    def test_there_are_exactly_the_correct_number_of_doors(self):
        hallway = Hallway(ARBITRARY_SMALL_NUM_DOORS)
        result = len(hallway.doors)
        expected = ARBITRARY_SMALL_NUM_DOORS
        assert result == expected

    def test_doors_are_closed_in_the_beginning(self):
        hallway = Hallway(ARBITRARY_SMALL_NUM_DOORS)
        result = all(door is CLOSED_DOOR for door in hallway.doors)
        expected = True
        assert result == expected

    def test_toggle_door__when_door_is_closed(self):
        hallway = Hallway(ARBITRARY_SMALL_NUM_DOORS)
        hallway.toggle_door(1)
        result = not hallway.is_door_open(0) and hallway.is_door_open(1)
        expected = True
        assert result == expected

    def test_toggle_door__when_door_is_open(self):
        hallway = Hallway(ARBITRARY_SMALL_NUM_DOORS)
        hallway.doors[1] = OPEN_DOOR
        hallway.toggle_door(1)
        result = hallway.is_door_open(1)
        expected = False
        assert result == expected

    def test_toggle_door__twice(self):
        hallway = Hallway(num_doors=1)
        hallway.toggle_door(0)
        hallway.toggle_door(0)
        result = hallway.is_door_open(0)
        expected = False
        assert result == expected

    def test_toggle_door__three_times(self):
        hallway = Hallway(num_doors=1)
        hallway.toggle_door(0)
        hallway.toggle_door(0)
        hallway.toggle_door(0)
        result = hallway.is_door_open(0)
        expected = True
        assert result == expected

    def test_get_open_doors(self):
        hallway = Hallway(ARBITRARY_NUM_DOORS)
        hallway.doors[1] = OPEN_DOOR
        hallway.doors[3] = OPEN_DOOR
        result = list(hallway.get_open_doors())
        expected = [2, 4]
        assert result == expected

    def test_traverse_once(self):
        hallway = Hallway(ARBITRARY_SMALL_NUM_DOORS)
        hallway.traverse()
        result = all(door is OPEN_DOOR for door in hallway.doors)
        expected = True
        assert result == expected

    def test_traverse_twice(self):
        hallway = Hallway(ARBITRARY_NUM_DOORS)
        hallway.traverse()
        hallway.traverse()
        result = all(door is CLOSED_DOOR for door in hallway.doors)
        expected = True
        assert result == expected

    def test_traverse_two_steps(self):
        hallway = Hallway(ARBITRARY_NUM_DOORS)
        hallway.traverse(steps=2)
        result = [door is OPEN_DOOR for door in hallway.doors]
        expected = [CLOSED_DOOR, OPEN_DOOR, CLOSED_DOOR, OPEN_DOOR]
        assert result == expected

    def test_traverse_3_steps(self):
        hallway = Hallway(ARBITRARY_NUM_DOORS)
        hallway.traverse(steps=3)
        result = [door is OPEN_DOOR for door in hallway.doors]
        expected = [CLOSED_DOOR, CLOSED_DOOR, OPEN_DOOR, CLOSED_DOOR]
        assert result == expected

    def test_traverse_num_doors_times__for_four_doors(self):
        hallway = Hallway(4)
        hallway.traverse_num_doors_times()
        result = [door is OPEN_DOOR for door in hallway.doors]
        expected = [OPEN_DOOR, CLOSED_DOOR, CLOSED_DOOR, OPEN_DOOR]
        assert result == expected

    def test_traverse_num_doors_times__for_twenty_doors_and_get_open_doors(self):
        hallway = Hallway(num_doors=20)
        hallway.traverse_num_doors_times()
        result = list(hallway.get_open_doors())
        expected = [1, 4, 9, 16]
        assert result == expected

    def test_correct_output(self):
        hallway = Hallway(num_doors=100)
        hallway.traverse_num_doors_times()
        result = list(hallway.get_open_doors())
        expected = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
        assert result == expected
        print(f"Output: \nOpen doors:\n{result}\n"
              f"All the other doors are closed.\n")
