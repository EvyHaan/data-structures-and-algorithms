def insertion_sort(lst):
    for i in range(1, len(lst)):
        current_idx = i
        temp_val = lst[i]

        while current_idx > 0 and lst[current_idx - 1] > temp_val:
            lst[current_idx] = lst[current_idx - 1]
            current_idx = current_idx - 1

        lst[current_idx] = temp_val

    return lst
