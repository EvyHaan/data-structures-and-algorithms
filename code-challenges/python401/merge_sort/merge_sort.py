def merge_sort(lst):
    lst_len = len(lst)

    if lst_len > 1:
        left_lst, right_lst = merge_sort(lst[0:lst_len//2])
        right_lst = merge_sort(lst[lst_len//2:])

        sorted_lst = []
        i = 0
        j = 0

        while left_lst and right_lst:
            if left_lst[i] < right_lst[j]:
                sorted_lst.append(left_lst[i])
                i += 1
            else:
                sorted_lst.append(right_lst[j])
                j += 1

        if left_lst:
            sorted_lst.append(left_lst[i:])

        if right_lst:
            sorted_lst.append(right_lst[j:])

        return sorted_lst
