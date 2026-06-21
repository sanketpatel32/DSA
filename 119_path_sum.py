"""
119_path_sum

Question:
Return True if a root-to-leaf path sums to targetSum.

Input: root=[5,4,8,...], targetSum=22
Output: True

Approaches:
  1. Recursion subtracting node value from target  ->  O(n) time, O(h) space
  2. Iterative DFS with (node, remaining) stack  ->  O(n) time, O(h) space
  3. BFS with (node, remaining) queue  ->  O(n) time, O(w) space
"""

# TODO: implement your solution here