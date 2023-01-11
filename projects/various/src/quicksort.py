def _partition(list_, low, high):
    """Finds the partition position using the last element as the pivot."""
    pivot = list_[high]
    i = low - 1
    for j in range(low, high):
        if pivot > list_[j]:
            i = i + 1
            list_[i], list_[j] = list_[j], list_[i]
    # Swap the pivot element with the greater element, i
    list_[i + 1], list_[high] = list_[high], list_[i + 1]
    # Return the position from where the partition is done
    return i + 1


def quicksort(list_, low=0, high=None):
    """Sorts a list of elements using the quicksort algorithm with '_partition' as a help function."""
    if high is None:
        high = len(list_) - 1

    if low < high:
        pivot = _partition(list_, low, high)
        # Sort the left of the pivot
        quicksort(list_, low, pivot - 1)
        # Sort the right of the pivot
        quicksort(list_, pivot + 1, high)
