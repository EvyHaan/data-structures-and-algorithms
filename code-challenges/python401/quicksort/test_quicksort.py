from quicksort import quicksort


def test_randomly_unsorted_list():
    """An unsorted list returns sorted"""
    lst = [3, 2, 4, 5, 1]

    expected = [1, 2, 3, 4, 5]
    actual = quicksort(lst)
    assert actual == expected


# def test_sorted_list():
#     """A sorted list will return unchanged"""
#     lst = ['A', 'B', 'C', 'D', 'E']

#     expected = ['A', 'B', 'C', 'D', 'E']
#     actual = quicksort(lst)
#     assert actual == expected


# def test_backward_list():
#     """A backward list will return reversed"""
#     lst = ['E', 'D', 'C', 'B', 'A']

#     expected = ['A', 'B', 'C', 'D', 'E']
#     actual = quicksort(lst)
#     assert actual == expected


# def test_empty_list():
#     """An empty list will return unchanged"""
#     lst = []

#     expected = []
#     actual = quicksort(lst)
#     assert actual == expected


# def test_single_item_list():
#     """A one-itemed list will return unchanged"""
#     lst = ['A']

#     expected = ['A']
#     actual = quicksort(lst)
#     assert actual == expected
