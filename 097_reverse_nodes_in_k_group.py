"""
097_reverse_nodes_in_k_group

Question:
Reverse nodes in groups of k; leftover stay.

Input: head=[1,2,3,4,5], k=2
Output: [2,1,4,3,5]

Approaches:
  1. Iterative: count k, reverse group, link  ->  O(n) time, O(1) space
  2. Recursive reversal of groups  ->  O(n) time, O(n/k) stack
"""

# TODO: implement your solution here