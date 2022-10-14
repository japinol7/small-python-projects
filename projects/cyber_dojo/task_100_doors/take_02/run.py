from hallway import Hallway


def main():
    hallway = Hallway(num_doors=100)
    print(f"Output: \nOpen doors:\n{list(hallway.get_doors_to_open())}\n"
          f"All the other doors are closed.\n")


if __name__ == '__main__':
    main()
