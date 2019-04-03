# Quick Sort


## Challenge
Create a function that uses quicksort to return a sorted array.

## Approach & Efficiency
#### Approach
If the length of the given list is >= 1, it is considered sorted and can be returned. If it is longer than 1, then the value at the last index is set to be the pivot point, and left and right indicators are set at the first and last of the remaining indexes. The left indicator moves up the list until it hits a value that is greater than the pivot value or it hits the right indicator. If the former, then the right indicator moves down the list until it hits a value that is less than the pivot value or hits the left indicator. If the left indicator hits a value greater than the pivot value and the right indicator hits a value that is less than the pivot value, they swap values and continue moving up or down the list, respectively. If one indicator runs into the other, then the value of the left indicator is compared to the pivot value, and if it is greater, they switch. If they switch, the pivot position is reassigned to point to the position of the left indicator. The list is broken into sub-lists at this point and each sub-list runs through the function via recursion.
Once each subsequent sub-list has been sorted, the final mutated list is returned.

#### Efficiency
- Space: O(n)    **while the output is the list sorted in place, the slice method is used and has space efficiency consequences
- Time: O(n log n)

## Solution
![quicksort](https://github.com/EvyHaan/data-structures-and-algorithms/blob/master/code-challenges/python401/quicksort/assets/quicksort.jpg)