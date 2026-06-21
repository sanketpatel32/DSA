"""
123_binary_tree_postorder_traversal

Question:
Return postorder (left,right,root) traversal.

Input: root = [1,null,2,3]
Output: [3,2,1]

Approaches:
  1. Recursion  ->  O(n) time, O(h) space
  2. Iterative with reversed preorder (root,right,left) reversed  ->  O(n) time, O(h) space
  3. Iterative with explicit last-visited flag  ->  O(n) time, O(h) space
  4. Morris postorder variant  ->  O(n) time, O(1) space
"""

# TODO: implement your solution here