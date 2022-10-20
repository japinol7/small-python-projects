from time_it.time_it import time_it


def split_list_in_chunks(nums, n_chunks):
    """Split sequence in chunks of similar size."""
    k, m = divmod(len(nums), n_chunks)
    for i in range(n_chunks):
        yield nums[i * k + min(i, m): (i + 1) * k + min(i + 1, m)]


def main():
    input_n_chunks, input_nums = 3, [2, 1, 5, 1, 2, 2, 2]
    result = time_it(split_list_in_chunks, input_nums, input_n_chunks)
    result = list(result)
    print(f'Res: {result}')


if __name__ == '__main__':
    main()
