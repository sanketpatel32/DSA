"""
155_jump_game

Question:
Return True if you can reach the last index.

Input: nums = [2,3,1,1,4]
Output: True

Approaches:
  1. Recursion with memoization  ->  O(n^2) time, O(n) space
  2. DP from right tracking reachability  ->  O(n^2) time, O(n) space
  3. Greedy: track furthest reachable index  ->  O(n) time, O(1) space
"""

# TODO: implement your solution here