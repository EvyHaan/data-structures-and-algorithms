# Hashmap LEFT JOIN

## Challenge
Given two hashtables, perform a left join.

## Approach & Efficiency
#### Approach
1. Iterate through the first hashtable, and for each key in any bucket, compare the value to the same key in the second hashtable. If a match exists, append a list of the key, the value for the key at the first table, and the value for the key in the second table. If no match exists, append a list with the same first two items and include None as the third item in the list. Return a list of lists.

## Solution
![left_join](https://github.com/EvyHaan/data-structures-and-algorithms/blob/master/code-challenges/python401/left_join_hashtable/assets/left_join.jpg)