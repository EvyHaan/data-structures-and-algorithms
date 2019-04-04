def radix_sort(lst):
    if len(lst) <= 1:
        return lst

    if len(lst) > 1:
        digitmax = max(lst)
        exp = 1

        while (digitmax + 1) / exp > 1:
            sortd = sorting_hat(lst, exp)
            exp *= 10

        return sortd


def sorting_hat(lst, exp):
    presorted = []
    nunnery = [[]] * 10
    n = 0

    for num in lst:
        print(n, 'num: ' + str(num))
        sort_idx = (num // 10 ** n) % 10

        if not nunnery[sort_idx]:
            nunnery.insert(sort_idx, [num])
        else:
            nunnery[sort_idx] += [num]
        n += 1

    print(nunnery)
    for i in range(len(nunnery)):
        presorted += nunnery[i]
        print(presorted)

    return presorted
