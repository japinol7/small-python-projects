from take_01.hallway import Hallway


def main():
    hallway = Hallway(num_doors=100)
    hallway.traverse_num_doors_times()
    print(f"Output: \nOpen doors:\n{hallway.get_open_doors()}\n"
          f"All the other doors are closed.\n")


if __name__ == '__main__':
    main()
