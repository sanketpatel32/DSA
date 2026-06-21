"""
138_lowest_common_ancestor_of_a_binary_search_tree

Question:
Find LCA of two nodes in a BST using BST properties.

Input: root=[6,2,8,...], p=2, q=8
Output: 6

Approaches:
  1. Iteration: go toward node containing both p and q  ->  O(h) time, O(1) space
  2. Recursion exploiting BST ordering  ->  O(h) time, O(h) stack
"""

# TODO: implement your solution here