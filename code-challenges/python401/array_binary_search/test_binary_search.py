from array_binary_search import binary_search

def test_binarysearch_even():
    input_arr = ['a', 'b', 'c', 'd', 'e', 'f']
    input_target = 'b'

    actual = binary_search(input_arr, input_target)
    expected = 1
    assert expected == actual

# def test_binarysearch_odd():
#     input_arr = [3, 6, 9, 12, 18, 21, 24]
#     input_target = 24

#     actual = binary_search(input_arr, input_target)
#     expected = 6
#     assert expected == actual

# def test_binarysearch_no_target():
#     input_arr = [3, 6, 9, 12, 18, 21]
#     input_target = 17

#     actual = binary_search(input_arr, input_target)
#     expected = -1
#     assert expected == actual

# def test_binarysearch_empty_array():
#     input_arr = []
#     input_target = 6

#     actual = binary_search(input_arr, input_target)
#     expected = -1
#     assert expected == actual


# Tests
# 1 Test an even-length valid array and a target value that is present (str)
# 2 Test an odd-length valid array and a target value that is present (int)
# 3 Test a valid array and a target value that is not present
# 4 Test an empty array with a target value