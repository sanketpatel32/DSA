"""
124_binary_tree_level_order_traversal

Question:
Return level order (BFS) traversal grouped by level.

Input: root = [3,9,20,null,null,15,7]
Output: [[3],[9,20],[15,7]]

Approaches:
  1. BFS with queue, one level per iteration  ->  O(n) time, O(w) space
  2. Recursion with depth-indexed list  ->  O(n) time, O(h) space
"""

# TODO: implement your solution here