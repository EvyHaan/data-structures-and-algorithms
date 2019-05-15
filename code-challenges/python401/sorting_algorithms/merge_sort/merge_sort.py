def merge_sort(lst):
    """Returns a sorted array.

    A provided list will be sorted out-of-place.

    Args:
        list: a list to be sorted.

    Returns:
        list: a new list, sorted from least to greatest.
    """
    lst_len = len(lst)

    if lst_len <= 1:
        return lst

    if lst_len > 1:
        left_lst = merge_sort(lst[0:lst_len//2])
        right_lst = merge_sort(lst[lst_len//2:])

        sorted_lst = []

        while left_lst and right_lst:
            if left_lst[0] < right_lst[0]:
                sorted_lst.append(left_lst.pop(0))

            else:
                sorted_lst.append(right_lst.pop(0))

        if left_lst:
            sorted_lst += left_lst

        if right_lst:
            sorted_lst += right_lst

        return sorted_lst
