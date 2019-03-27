# Intersection of binary trees

## Challenge
Given two binary trees, return the values that can be found in both.

## Approach & Efficiency
The first tree is traversed, and on each visit to a node, the node's value is added to a hash table. The second tree is traversed, and on each visit to a node,the node's value is searched for in the hash table, and if it is found, it is added to an array. After the final visit, the array is returned.

#### Big O
- Space: O(n)
- Time: O(n)

## Solution
![tree_intersection](https://github.com/EvyHaan/data-structures-and-algorithms/blob/master/code-challenges/python401/tree_intersection/assets/tree_intersection.jpg)