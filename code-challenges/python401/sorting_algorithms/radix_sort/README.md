# Radix Sort


## Challenge
Create a function that uses merge sort to return a sorted array.

## Approach & Efficiency
#### Approach
If the length of the given list is >= 1, it is considered sorted and can be returned. If not, sort the numbers out into buckets, by their 1's place digit and concatenate the buckets back into the list. Successivly sort and concatenate the newly organized list in the same way by their 10's, 100's, etc digit up until that position matches that of the longest number. Return the resulting list.

#### Efficiency
- Space: O(n)
- Time: O(n)

## Solution
![merge_sort](https://github.com/EvyHaan/data-structures-and-algorithms/blob/master/code-challenges/python401/radix_sort/assets/radix_sort.jpg)