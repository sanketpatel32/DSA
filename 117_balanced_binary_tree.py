"""
117_balanced_binary_tree

Question:
Return True if the tree is height-balanced.

Input: root = [3,9,20,null,null,15,7]
Output: True

Approaches:
  1. Top-down: check heights at each node (recompute)  ->  O(n^2) time, O(h) space
  2. Bottom-up: return height or -1 if unbalanced  ->  O(n) time, O(h) space
"""

# TODO: implement your solution here