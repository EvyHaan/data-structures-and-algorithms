def radix_sort(lst):
    """Returns a sorted array.

#     A provided list will be sorted out-of-place.

#     Args:
#         lst: a list to be sorted.

#     Returns:
#         lst: the mutated list, sorted from least to greatest.
#     """
    if len(lst) <= 1:
        return lst

    max_digit = len(str(max(lst)))
    exp = 0

    while max_digit > exp:
        nunnery = [None] * 10

        while lst:
            idx = (lst[0] // 10 ** exp) % 10
            if nunnery[idx] is None:
                nunnery[idx] = [lst.pop(0)]
            else:
                nunnery[idx].append(lst.pop(0))

        for bucket in nunnery:
            if bucket is not None:
                lst += bucket

        exp += 1

    return lst
