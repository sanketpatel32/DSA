"""
136_validate_binary_search_tree

Question:
Return True if the binary tree is a valid BST.

Input: root = [2,1,3]
Output: True

Approaches:
  1. Inorder traversal must be strictly increasing  ->  O(n) time, O(h) space
  2. Recursion with (min,max) bounds  ->  O(n) time, O(h) space
"""

# TODO: implement your solution here