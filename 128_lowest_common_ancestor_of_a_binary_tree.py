"""
128_lowest_common_ancestor_of_a_binary_tree

Question:
Find LCA of two nodes p and q.

Input: root=[3,5,1,...], p=5, q=1
Output: 3

Approaches:
  1. Recursion: node where both sides return or node==p/q  ->  O(n) time, O(h) space
  2. Iterative with parent pointers + ancestor set  ->  O(n) time, O(n) space
"""

# TODO: implement your solution here