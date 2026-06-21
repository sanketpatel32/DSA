"""
135_delete_node_in_a_bst

Question:
Delete node with key from BST preserving properties.

Input: root=[5,3,6,2,4,null,7], key=3
Output: modified BST

Approaches:
  1. Recursion: replace with inorder successor/predecessor on match  ->  O(h) time, O(h) space
  2. Iteration with parent tracking  ->  O(h) time, O(1) space
"""

# TODO: implement your solution here