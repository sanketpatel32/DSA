"""
137_kth_smallest_element_in_a_bst

Question:
Return kth smallest element (1-indexed).

Input: root=[3,1,4,null,2], k=1
Output: 1

Approaches:
  1. Inorder traversal collecting k elements  ->  O(h+k) time, O(h) space
  2. Iterative inorder stack stopping at k  ->  O(h+k) time, O(h) space
"""

# TODO: implement your solution here