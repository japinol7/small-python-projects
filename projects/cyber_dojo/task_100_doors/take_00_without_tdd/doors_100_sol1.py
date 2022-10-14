
def get_final_open_doors(num_doors):
    # Add 1 more door because we will ignore door number 0
    num_doors += 1

    doors = [False for _ in range(num_doors)]
    counter = 1
    while counter <= num_doors:
        for i in range(counter, num_doors, counter):
            doors[i] = not doors[i]
        counter += 1
    return [(door, 'open' if state else 'closed')
            for door, state in enumerate(doors) if door > 0]


def main():
    doors = get_final_open_doors(num_doors=100)
    result = [d for d, state in doors if state == 'open']
    print(f"Open doors: {result}")

    expected = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
    print(f"{'-' * 25}\n Inline test: "
          f"{'OK' if result == expected else 'FAILED'}")


if __name__ == '__main__':
    main()
