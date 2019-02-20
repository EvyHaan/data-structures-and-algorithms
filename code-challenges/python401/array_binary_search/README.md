# List Binary Search

## Challenge
Write a function which takes in a sorted array and a search key and returns the index of the array's element that is equal to the search key, or -1 if the search key is not found.

## Approach & Efficiency
Big 0 -- Time: O(logN) -- Space: O(N)

In this approach, the function compares the value of the middle position of the array to the target. If it matches, the index is returned. Otherwise it adjusts the left or right bounds of the search area to eliminate sections of the array that logically would not contain the element until the element is either found or determined to not to be in the given array.

## Solution
![binary_search](img link here)