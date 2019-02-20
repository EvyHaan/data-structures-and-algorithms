from array_shift import insertShiftArray

def test_even_array():
    original_arr = [1, 2, 4, 5]
    original_val = 3

    actual = insertShiftArray(original_arr, original_val)
    expected = [1, 2, 3, 4, 5]
    assert expected == actual

def test_odd_array():
    original_arr = [1, 2, 3, 5, 6]
    original_val = 4

    actual = insertShiftArray(original_arr, original_val)
    expected = [1, 2, 3, 4, 5, 6]
    assert expected == actual

def test_odd_array_2():
    original_arr = [1, 2, 3, 5, 6]
    original_val = 8

    actual = insertShiftArray(original_arr, original_val)
    expected = [1, 2, 3, 8, 5, 6]
    assert expected == actual

def test_empty_array():
    original_arr = []
    original_val = 1

    actual = insertShiftArray(original_arr, original_val)
    expected = [1]
    assert expected == actual

# Test for an array of even length
# Test for an array of odd length
# Test for an empty array

