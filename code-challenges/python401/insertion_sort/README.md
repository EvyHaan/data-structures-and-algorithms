# Insertion Sort


## Challenge
Create a function that uses insertion sort to return a sorted array.

## Approach & Efficiency
#### Approach
Starting at index 1, store the value in a temporary variable and compare consecutive values to the left to this temporary variable. Once a value is found that is less than the temporary value, insert the temporary value back into the array. Repeat this process with subsequent indices.

#### Efficiency
- Space: O(1)
- Time: O(n^2)
