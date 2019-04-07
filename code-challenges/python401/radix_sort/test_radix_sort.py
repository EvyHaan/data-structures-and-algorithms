from radix_sort import radix_sort


def test_empty_list():
    """An empty list will return unchanged"""
    lst = []

    expected = []
    actual = radix_sort(lst)
    assert actual == expected


def test_single_item_list():
    """A one-itemed list will return unchanged"""
    lst = [100]

    expected = [100]
    actual = radix_sort(lst)
    assert actual == expected


def test_sorted_list():
    """A sorted list will return unchanged"""
    lst = [1, 22, 23, 35, 586, 1476]

    expected = [1, 22, 23, 35, 586, 1476]
    actual = radix_sort(lst)
    assert actual == expected

def test_randomly_unsorted_list():
    """An unsorted list returns sorted"""
    lst = [23, 22, 476, 35, 1, 86]

    expected = [1, 22, 23, 35, 86, 476]
    actual = radix_sort(lst)
    assert actual == expected



def test_backward_list():
    """A backward list will return reversed"""
    lst = [1476, 586, 35, 23, 22, 1]

    expected = [1, 22, 23, 35, 586, 1476]
    actual = radix_sort(lst)
    assert actual == expected
