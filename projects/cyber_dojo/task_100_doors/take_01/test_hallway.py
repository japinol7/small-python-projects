from hallway import Hallway


class TestHallway:
    def test_doors_are_closed_in_the_beginning(self):
        # All the doors should be False, which means they are closed
        hallway = Hallway(num_doors=2)
        result = not any(door for door in hallway.doors)
        expected = True
        assert result == expected

    def test_there_are_exactly_the_correct_number_of_doors(self):
        hallway = Hallway(num_doors=3)
        result = len(hallway.doors)
        expected = 3
        assert result == expected

    def test_is_door_open__in_the_beginning(self):
        hallway = Hallway(num_doors=1)
        result = hallway.is_door_open(0)
        expected = False
        assert result == expected

    def test_is_door_open__after_being_opened(self):
        hallway = Hallway(num_doors=1)
        hallway.open_door(0)
        result = hallway.is_door_open(0)
        expected = True
        assert result == expected

    def test_is_door_open__false_after_being_closed(self):
        hallway = Hallway(num_doors=1)
        hallway.open_door(0)
        hallway.close_door(0)
        result = hallway.is_door_open(0)
        expected = False
        assert result == expected

    def test_toggle_door__when_door_is_closed(self):
        hallway = Hallway(num_doors=1)
        hallway.close_door(0)
        hallway.toggle_door(0)
        result = hallway.is_door_open(0)
        expected = True
        assert result == expected

    def test_toggle_door__when_door_is_open(self):
        hallway = Hallway(num_doors=1)
        hallway.open_door(0)
        hallway.toggle_door(0)
        result = hallway.is_door_open(0)
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

    def test_traverse(self):
        hallway = Hallway(num_doors=4)
        hallway.traverse()
        result = hallway.doors
        expected = [True, True, True, True]
        assert result == expected

    def test_traverse_twice(self):
        hallway = Hallway(num_doors=4)
        hallway.traverse()
        hallway.traverse()
        result = hallway.doors
        expected = [False, False, False, False]
        assert result == expected

    def test_traverse_two_steps(self):
        hallway = Hallway(num_doors=4)
        hallway.traverse(steps=2)
        result = hallway.doors
        expected = [False, True, False, True]
        assert result == expected

    def test_traverse_num_doors_times__for_four_doors(self):
        hallway = Hallway(num_doors=4)
        hallway.traverse_num_doors_times()
        result = hallway.doors
        expected = [True, False, False, True]
        assert result == expected

    def test_traverse_num_doors_times__for_four_doors_and_get_open_doors(self):
        hallway = Hallway(num_doors=4)
        hallway.traverse_num_doors_times()
        result = list(hallway.get_open_doors())
        expected = [1, 4]
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
