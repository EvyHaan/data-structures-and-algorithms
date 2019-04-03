def quicksort(lst):

    if len(lst) <= 1:
        return lst

    if len(lst) > 1:
        pivot = len(lst) - 1
        left = 0
        right = pivot - 1

        while lst[left] < lst[pivot] and left != right:
            left += 1

        while lst[right] < lst[pivot] and right != left:
            right -= 1

        if lst[left] >= lst[pivot] and lst[right] <= lst[pivot]:
            lst[left], lst[right] = lst[right], lst[left]

        if left == right:
            if lst[left] > lst[pivot]:
                lst[left], lst[pivot] = lst[pivot], lst[left]

        left_lst = quicksort(lst[:left])
        right_lst = quicksort(lst[(left + 1):])

    return lst
