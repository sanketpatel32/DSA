"""
233_fenwick_tree_implementation

Question:
Implement a Fenwick (BIT) with prefix sum and point update.

Input: arr=[2,1,1,3,...]
Output: queries

Approaches:
  1. Fenwick tree with lowbit indexing  ->  O(log n) update/query, O(n) space
  2. With range update + point query variant  ->  O(log n), O(n) space
"""

# TODO: implement your solution here