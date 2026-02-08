def main():
    data = list(range(1, 8))
    data_len = len(data)

    for i in range(data_len):
        for j in range(i, data_len):
            print(data[i: j + 1], end='')
        print()


if __name__ == '__main__':
    main()
