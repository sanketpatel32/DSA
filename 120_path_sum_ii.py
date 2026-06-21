"""
120_path_sum_ii

Question:
Return all root-to-leaf paths summing to targetSum.

Input: root=[5,4,8,...], targetSum=22
Output: [[5,4,11,2]]

Approaches:
  1. Backtracking with current path and remaining sum  ->  O(n^2) time, O(h) space
  2. DFS copying path at each leaf  ->  O(n^2) time, O(n*h) space
"""

# TODO: implement your solution here