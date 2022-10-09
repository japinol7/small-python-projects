
def get_final_open_doors(num_doors):
    doors = []
    for i in range(1, num_doors + 1):
        if i ** 0.5 % 1:
            state = 'closed'
        else:
            state = 'open'
        doors.append((i, state))
    return doors


def main():
    doors = get_final_open_doors(num_doors=100)
    result = [d for d, state in doors if state == 'open']
    print(f"Open doors: {result}")

    expected = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
    print(f"{'-' * 25}\n Inline test: "
          f"{'OK' if result == expected else 'FAILED'}")


if __name__ == '__main__':
    main()
