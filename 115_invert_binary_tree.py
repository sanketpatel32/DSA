"""
115_invert_binary_tree

Question:
Invert a binary tree (swap children recursively).

Input: root = [4,2,7,1,3,6,9]
Output: [4,7,2,9,6,3,1]

Approaches:
  1. Recursion swapping children  ->  O(n) time, O(h) space
  2. Iterative BFS swapping children level by level  ->  O(n) time, O(w) space
  3. Iterative stack DFS swapping  ->  O(n) time, O(h) space
"""

# TODO: implement your solution here