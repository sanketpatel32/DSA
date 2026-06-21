"""
122_binary_tree_inorder_traversal

Question:
Return inorder (left,root,right) traversal.

Input: root = [1,null,2,3]
Output: [1,3,2]

Approaches:
  1. Recursion  ->  O(n) time, O(h) space
  2. Iterative stack going left then popping  ->  O(n) time, O(h) space
  3. Morris traversal (threaded, O(1) space)  ->  O(n) time, O(1) space
"""

# TODO: implement your solution here