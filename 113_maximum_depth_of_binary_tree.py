"""
113_maximum_depth_of_binary_tree

Question:
Return the maximum depth of a binary tree.

Input: root = [3,9,20,null,null,15,7]
Output: 3

Approaches:
  1. Recursion: 1 + max(depth(left), depth(right))  ->  O(n) time, O(h) stack
  2. BFS counting levels  ->  O(n) time, O(w) space
  3. Iterative DFS with (node,depth) stack  ->  O(n) time, O(h) space
"""

# TODO: implement your solution here