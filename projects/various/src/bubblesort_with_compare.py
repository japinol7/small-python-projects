def bubblesort_with_compare(list_, compare_func):
    list_len = len(list_)
    some_swap = False
    for i in range(list_len - 1):
        for j in range(0, list_len - i - 1):
            if compare_func(list_[j], list_[j + 1]):
                list_[j], list_[j + 1] = list_[j + 1], list_[j]
                some_swap = True
        if not some_swap:
            break
