def _partition(list_, compare_func, low, high):
    """Finds the partition position using the last element as the pivot."""
    pivot = list_[high]
    i = low - 1
    for j in range(low, high):
        if compare_func(pivot, list_[j]):
            i = i + 1
            list_[i], list_[j] = list_[j], list_[i]
    # Swap the pivot element with the greater element, i
    list_[i + 1], list_[high] = list_[high], list_[i + 1]
    # Return the position from where the partition is done
    return i + 1


def quicksort_with_compare(list_, compare_func, low=0, high=None):
    """Sorts a list of elements using the quicksort algorithm with '_partition' as a help function.
    Also, this version requires a compare function to make the comparison of the pivot
    with the other item.
    """
    if high is None:
        high = len(list_) - 1

    if low < high:
        pivot = _partition(list_, compare_func, low, high)
        # Sort the left of the pivot
        quicksort_with_compare(list_, compare_func, low, pivot - 1)
        # Sort the right of the pivot
        quicksort_with_compare(list_, compare_func, pivot + 1, high)
