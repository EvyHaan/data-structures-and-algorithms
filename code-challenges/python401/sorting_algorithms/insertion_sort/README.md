# Insertion Sort


## Challenge
Implement an insert sort function.

## Approach & Efficiency
### Approach

Given a list, we assume the item at index 0 is in the correct position.

For each item starting at index 1 and moving through the range of the list:
1. a index reference is assigned to the current index.
2. the value of the item at the current index is stored in a temporary variable.
3. while the current index reference is greater than 0 AND the value to the left of the current index is larger than the value of the temporary variable, the value where the temporary varable was previously is reassigned to the value to the left, and the index reference is reassigned to one index prior.
4. once either of the above conditions is not met, the value at the current index reference is assigned to the temporary value.

The list is returned. It has been sorted in-place.

### Efficiency

|SCENARIO:|  BEST   |   AVG   |  WORST  |
|---------|---------|---------|---------|
| TIME    |  O(n)   | O(n^2)  | O(n^2)  |
| SPACE   |  O(1)   | O(1)    | O(1)    |