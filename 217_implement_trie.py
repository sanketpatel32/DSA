"""
217_implement_trie

Question:
Implement a Trie with insert/search/startsWith.

Input: insert('apple'), search('apple')
Output: True

Approaches:
  1. Array-based children (size 26) per node  ->  O(L) per op, O(N*L) space
  2. Hash map children per node  ->  O(L) per op, O(N*L) space
"""

# TODO: implement your solution here