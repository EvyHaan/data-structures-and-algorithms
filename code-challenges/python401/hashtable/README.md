# Hashtables

## Challenge
Write a Hashtable class that has the methods hash(), add(), get(), and contains()

## Approach & Efficiency
Big O
hash: - space: O(1) -- time: O(1) -
add: - space: O(n) -- time: O(n) -
get: - space: O(1) -- time: O(n) -
contains: - space: O(1) -- time: O(n) -

## API
.hash(): takes in a key and returns an index in a hash table where it can be stored
.add(): takes in a key and a value, finds the hashed value of the key to determine the index at which it can be stored, and inserts it to that index.
.get(): takes in a key, searches the hashtable, and retrieves the value if it exists.
.contains(): takes in a key, and returns a boolean if the hashtable contains it or not.