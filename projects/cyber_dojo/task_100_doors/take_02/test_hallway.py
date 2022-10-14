from hallway import Hallway


class TestHallway:
    def test_number_of_doors(self):
        hallway = Hallway(num_doors=3)
        result = hallway.num_doors
        expected = 3
        assert result == expected

    def test_get_doors_to_open_correct_output(self):
        hallway = Hallway(num_doors=100)
        result = list(hallway.get_doors_to_open())
        expected = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
        assert result == expected
        print(f"Output: \nOpen doors:\n{result}\n"
              f"All the other doors are closed.\n")
