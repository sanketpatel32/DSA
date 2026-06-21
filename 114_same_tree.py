"""
114_same_tree

Question:
Return True if two binary trees are identical.

Input: p=[1,2,3], q=[1,2,3]
Output: True

Approaches:
  1. Recursion comparing roots then subtrees  ->  O(n) time, O(h) space
  2. Iterative DFS with parallel stacks  ->  O(n) time, O(h) space
  3. BFS with parallel queues  ->  O(n) time, O(w) space
"""

# TODO: implement your solution here