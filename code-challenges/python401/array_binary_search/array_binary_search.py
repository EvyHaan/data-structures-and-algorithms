"""
This module conducts a binary search.
"""

def binary_search(arr, target):
    """
    A function that conducts a binary search for a target in a sorted list.

    Parameters:
        arr (list): The list to be searched.
        target (number, str): The target element to be searched for. 
    """"

    l_bound = 0
    r_bound = len(arr) - 1

    while l_bound <= r_bound:
        mid = (l_bound + r_bound) // 2

        if target < arr[mid]:
            r_bound = mid - 1
        elif target > arr[mid]:
            l_bound = mid + 1
        else:
            return(mid)

        return(-1)
