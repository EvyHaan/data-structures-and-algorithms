def quicksort(lst):
    """Returns a sorted array.

    A provided list will be sorted in place.

    Args:
        list: a list to be sorted.

    Returns:
        list: a new list, sorted from least to greatest.
    """

    if len(lst) <= 1:
        return lst

    if len(lst) > 1:
        pivot = len(lst) - 1
        left = 0
        right = pivot - 1

        while lst[left] < lst[pivot] and left != right:
            left += 1

        while lst[right] > lst[pivot] and right != left:
            right -= 1

        if lst[left] >= lst[pivot] and lst[right] <= lst[pivot]:
            lst[left], lst[right] = lst[right], lst[left]

        if lst[left] > lst[pivot]:
            lst[left], lst[pivot] = lst[pivot], lst[left]
            pivot = left

        left_lst = quicksort(lst[:pivot])
        right_lst = quicksort(lst[pivot + 1:])

        return left_lst + [lst[pivot]] + right_lst
