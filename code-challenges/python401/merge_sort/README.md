# Merge Sort


## Challenge
Create a function that uses merge sort to return a sorted array.

## Approach & Efficiency
#### Approach
If the length of the given list is >= 1, it is considered sorted and can be returned. If not, break the given list in half recursively until it becomes a series of lists of 1 item. Then compare items side by side and append them into a new output list in order of lowest to highest value. Return the resulting new list.

#### Efficiency
- Space: O(n)
- Time: O(n log n)

## Solution
![merge_sort](https://github.com/EvyHaan/data-structures-and-algorithms/blob/master/code-challenges/python401/merge_sort/assets/merge_sort.jpg)