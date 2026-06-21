"""
127_construct_binary_tree_from_preorder_and_inorder_traversal

Question:
Construct tree from preorder and inorder arrays.

Input: preorder=[3,9,20,15,7], inorder=[9,3,15,20,7]
Output: tree

Approaches:
  1. Recursion: root=preorder[0], split inorder at root, recurse  ->  O(n^2) time (linear search), O(n) space
  2. Recursion with inorder index map  ->  O(n) time, O(n) space
  3. Iterative with stack  ->  O(n) time, O(n) space
"""

# TODO: implement your solution here