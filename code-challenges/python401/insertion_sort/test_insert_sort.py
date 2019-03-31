from insert_sort import insertion_sort


def test_randomly_unsorted_list():
    """An unsorted list returns sorted"""
    lst = ['C', 'B', 'D', 'E', 'A']

    expected = ['A', 'B', 'C', 'D', 'E']
    actual = insertion_sort(lst)
    assert actual == expected


def test_sorted_list():
    """A sorted list will return unchanged"""
    lst = ['A', 'B', 'C', 'D', 'E']

    expected = ['A', 'B', 'C', 'D', 'E']
    actual = insertion_sort(lst)
    assert actual == expected


def test_backward_list():
    """A backward list will return reversed"""
    lst = ['E', 'D', 'C', 'B', 'A']

    expected = ['A', 'B', 'C', 'D', 'E']
    actual = insertion_sort(lst)
    assert actual == expected


def test_empty_list():
    """An empty list will return unchanged"""
    lst = []

    expected = []
    actual = insertion_sort(lst)
    assert actual == expected


def test_single_item_list():
    """A one-itemed list will return unchanged"""
    lst = ['A']

    expected = ['A']
    actual = insertion_sort(lst)
    assert actual == expected
